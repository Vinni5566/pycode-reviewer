# 🤖 Agentic sktime Assistant
### *LLM-driven Time Series Workflow Generator & Agentic Pipeline Builder*

[![sktime](https://img.shields.io/badge/powered%20by-sktime-orange.svg)](https://github.com/sktime/sktime)
[![ESoC 2024](https://img.shields.io/badge/ESoC-2024-blue.svg)](https://github.com/sktime/sktime/wiki/ESoC-2024)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Overview
The **Agentic sktime Assistant** is a specialized agentic framework designed to bridge the gap between natural language intent and executable `sktime` workflows. It addresses the steep learning curve of the `sktime` ecosystem by using LLMs to autonomously construct forecasting, classification, and transformation pipelines.

This project is a direct contribution to the **Enabling sktime Ecosystem (ESoC)** initiative, specifically targeting the **Agentic Forecaster** and **Agentic Tooling** tracks.

---

## 🎯 ESoC Alignment & Eligibility
This project fulfills the eligibility criteria for the `sktime` agentic track by implementing:
- **Agentic Pipeline Generation:** Converts English language prompts into valid `sktime` estimators and `ForecastingPipeline` objects.
- **RAG-Grounded Reasoning:** Utilizes a Retrieval-Augmented Generation (RAG) system over official `sktime` tutorials to ensure syntax correctness.
- **MCP-Ready Architecture:** Designed with a tool-calling layer compatible with the **Model Context Protocol (MCP)**, allowing it to integrate with prototypes like `sktime-mcp`.
- **Intelligent Evaluation:** Automatically generates performance metrics (e.g., MAPE) based on the suggested workflow.

---

## 🚀 Key Features
- **Intent Recognition:** Autonomously classifies queries into tasks (Forecasting, Anomaly Detection, etc.).
- **Smart Retrieval:** Uses FAISS to pull relevant code snippets from the `sktime` documentation.
- **Dynamic Tooling:** Exposes `sktime` primitives as callable tools for LLM agents.
- **Streamlit Dashboard:** A premium, interactive UI for experimenting with agentic workflows.
- **CLI Interface:** A robust command-line tool for developers.

---

## 🛠️ System Architecture
```mermaid
graph TD
    A[User Query] --> B[Intent Classifier]
    B --> C[FAISS Retriever]
    C --> D[sktime Docs / Tutorials]
    D --> E[LLM Agent]
    E --> F[Agentic Tools]
    F --> G[sktime Pipeline Code]
    G --> H[Execution / Explanation]
```

---

## 📦 Installation
```bash
# Clone the repository
git clone https://github.com/Vinni5566/pycode-reviewer.git
cd pycode-reviewer

# Install dependencies
pip install -r requirements.txt
```

---

## 🎮 Usage

### 1. Ingest Knowledge
Populate the RAG system with the latest `sktime` tutorial notebooks:
```bash
python scripts/fetch_docs.py
```

### 2. Interactive Dashboard
Run the premium Streamlit UI:
```bash
streamlit run sktime_agent/app.py
```

### 3. CLI Assistant
```bash
# Get a dummy workflow (Quick Demo)
python -m sktime_agent.cli "forecast sales for 12 months"

# Get a real LLM-reasoned workflow (Requires API Key)
python -m sktime_agent.cli "compare ARIMA vs Exponential Smoothing" --agent
```

---

## 📝 Roadmap & Future Extensions
- [ ] **Full sktime-mcp Integration:** Direct connection to the `sktime-mcp` server.
- [ ] **Data-Aware Pipeline Building:** Allowing the agent to inspect user data before suggesting estimators.
- [ ] **Foundation Model Support:** Integrating models like `Chronos` or `Lag-Llama` into the agent's toolbox.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
**Built for the Enabling sktime Ecosystem (ESoC) 2024.**
