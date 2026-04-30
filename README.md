# Agentic sktime Assistant: LLM-driven Time Series Workflow Generator

## Overview
`sktime` is a powerful and widely-used framework for time series analysis, but its extensive API can have a steep learning curve. The **Agentic sktime Assistant** is an LLM-powered tool designed to bridge the gap between natural language intent and executable `sktime` workflows.

This project is part of the **Enabling sktime Ecosystem (ESoC)** initiative, focusing on improving accessibility and automating complex time series pipelines through agentic intelligence.

## Core Features
- **Intent Recognition:** Automatically classifies user queries into tasks like forecasting, classification, regression, or anomaly detection.
- **RAG-Powered Retrieval:** Grounded in official `sktime` documentation and examples to ensure code correctness.
- **Workflow Generation:** Produces valid `sktime` pipeline code, detailed explanations, and optional evaluation steps.
- **Agentic Tooling:** Exposes `sktime` functionality as callable tools for advanced reasoning and multi-step pipeline building.

## System Architecture
1. **Input Layer:** Accepts natural language queries.
2. **Retrieval Layer (RAG):** Uses FAISS and sentence-transformers to retrieve relevant snippets from `sktime` docs.
3. **Agent Layer:** LLM reasoning to synthesize retrieved context into structured outputs.
4. **Tool Layer:** Wraps `sktime` functions as tools for the agent.
5. **Output Layer:** CLI-first interface with an optional Streamlit dashboard.

## Quick Start (MVP v1)
### Installation
```bash
pip install -r requirements.txt
```

### Usage
```bash
python -m sktime_agent.cli "forecast sales for the next 12 months"
```

## Project Roadmap (ESoC Alignment)
- [x] PR 1: Project Foundation & CLI Skeleton
- [ ] PR 2: sktime Knowledge Loader (Ingestion Pipeline)
- [ ] PR 3: Retrieval System (RAG with FAISS)
- [ ] PR 4: LLM Agent Core (Reasoning + Generation)
- [ ] PR 5: Tool Layer (sktime Agentic Interface)
- [ ] PR 6: Interactive Demo (Streamlit/CLI UI)

## License
MIT