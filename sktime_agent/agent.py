import os
from dotenv import load_dotenv
load_dotenv()
from typing import List
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from .core import AgentResponse
from .retrieval import SktimeRetriever

SYSTEM_PROMPT = """
You are an expert in the sktime Python library for time series analysis.
Your goal is to help users build forecasting, classification, and other time series pipelines.

Context from sktime documentation:
{context}

User Query: {query}

Instructions:
1. Identify the task type (forecasting, classification, regression, anomaly_detection).
2. Use valid sktime estimators and pipelines (e.g., ForecastingPipeline, TransformedTargetForecaster).
3. Provide a clear explanation of the approach.
4. Generate runnable Python code.
5. Provide an optional evaluation snippet.

Output your response as a valid JSON object with the following keys:
- task_type: The identified task.
- explanation: A brief explanation of the pipeline.
- code: The sktime code snippet.
- evaluation: An optional evaluation snippet.
"""

from .tools import SKTIME_TOOLS

class SktimeAgent:
    def __init__(self, model_name="gpt-4o", provider="openai"):
        self.retriever = SktimeRetriever()
        self.parser = JsonOutputParser(pydantic_object=AgentResponse)
        
        if provider == "openai":
            self.llm = ChatOpenAI(model=model_name, temperature=0).bind_tools(SKTIME_TOOLS)
        elif provider == "google":
            self.llm = ChatGoogleGenerativeAI(model=model_name, temperature=0).bind_tools(SKTIME_TOOLS)
        else:
            raise ValueError(f"Unsupported provider: {provider}")

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

        # 3. Chain and Invoke
        chain = prompt | self.llm | self.parser
        
        response_dict = chain.invoke({
            "context": context,
            "query": query
        })
        
        return AgentResponse(**response_dict)
