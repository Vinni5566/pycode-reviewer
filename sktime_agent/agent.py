import os
import json
import re
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from .core import AgentResponse
from .retrieval import SktimeRetriever

SYSTEM_PROMPT = """You are an expert in the sktime Python library for time series analysis.
Your goal is to help users build forecasting, classification, and other time series pipelines.

Context from sktime documentation:
{context}

User Query: {query}

Instructions:
1. Identify the task type: one of forecasting, classification, regression, or anomaly_detection.
2. Use valid sktime estimators and pipelines (e.g., ForecastingPipeline, TransformedTargetForecaster).
3. Provide a clear explanation of the approach.
4. Generate runnable Python code.
5. Provide an optional evaluation snippet.

You MUST respond with ONLY a raw JSON object. No markdown, no code fences, no explanation outside the JSON.
The JSON must have exactly these keys:
- task_type (string)
- explanation (string)
- code (string)
- evaluation (string or null)

Example format:
{{"task_type": "forecasting", "explanation": "...", "code": "...", "evaluation": "..."}}"""


class SktimeAgent:
    def __init__(self, model_name="gpt-4o", provider="openai"):
        self.retriever = SktimeRetriever()

        if provider == "openai":
            self.llm = ChatOpenAI(model=model_name, temperature=0)
        elif provider == "google":
            self.llm = ChatGoogleGenerativeAI(model=model_name, temperature=0)
        else:
            raise ValueError(f"Unsupported provider: {provider}")

    def _parse_response(self, raw: str) -> dict:
        """Robustly extract JSON from the model's raw text output."""
        # Strip markdown code fences if present
        raw = raw.strip()
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
        raw = raw.strip()
        return json.loads(raw)

    def generate_workflow(self, query: str) -> AgentResponse:
        # 1. Retrieve context
        try:
            docs = self.retriever.search(query, k=3)
            context = "\n\n".join([d.page_content for d in docs])
        except Exception:
            context = "No specific documentation found. Use general sktime knowledge."

        # 2. Build Prompt
        prompt = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_PROMPT),
            ("user", "{query}")
        ])

        # 3. Invoke LLM directly (no chained parser — we parse manually)
        chain = prompt | self.llm
        result = chain.invoke({"context": context, "query": query})
        raw_text = result.content

        # 4. Robust JSON parse
        response_dict = self._parse_response(raw_text)
        return AgentResponse(**response_dict)
