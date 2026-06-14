# AI Engineering

A Python-based AI engineering project using LangChain and Llama Index for Retrieval Augmented Generation (RAG). This project provides tools for querying documents and generating responses using NVIDIA's AI models.

## Features

- **RAG Pipeline**: Build retrieval-augmented generation applications using LangChain and Llama Index
- **NVIDIA Models**: Integration with NVIDIA's AI model stack (Llama 3, embeddings, multimodal models)
- **Document Processing**: Load and process documents from directories using SimpleDirectoryReader
- **Vector Search**: Create and query vector indexes for semantic search
- **Jupyter Notebooks**: Interactive development environment with pre-configured kernels

## Dependencies

- Python >= 3.13
- [LangChain](https://python.langchain.com/) - Modular LLM application framework
- [Llama Index](https://docs.llamaindex.ai/) - Data frameworks for LLM applications
- [NVIDIA AI Endpoints](https://github.com/langchain-ai/langchain-nvidia/) - NVIDIA AI model integrations
- JupyterLab - Interactive development environment

## Usage Example

```python
from dataclasses import dataclass
from dotenv import load_dotenv
from llama_index.llms.nvidia import NVIDIA
from llama_index.embeddings.nvidia import NVIDIAEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Load environment variables
load_dotenv()

# Initialize LLM with NVIDIA model
llm = NVIDIA(model="openai/gpt-oss-120b")

# Initialize embedding model
embedder = NVIDIAEmbedding(model="nvidia/nv-embedqa-e5-v5")

# Configure settings
@dataclass
class Settings:
    llm: NVIDIA
    embed_model: NVIDIAEmbedder

Settings.llm = llm
Settings.embed_model = embedder

# Load documents and create index
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# Query the index
response = query_engine.query("Which laptop is better?")
print(response)
```

## Project Structure

```
AI Engineering/
├── data/                  # Document files for RAG
│   ├── file4.txt          # Testing best practices for AI apps
│   ├── file5.txt          # Common API design mistakes
│   ├── file6.txt          # Authentication and authorization
│   └── file7.txt          # Vector databases for RAG
├── test_code.ipynb       # Example notebook with basic usage
├── rag_example.ipynb     # Real-world RAG example (code analysis)
├── pyproject.toml        # Python project configuration
├── .env                  # Environment variables (add your API keys)
└── README.md             # This file
```

## Quick Start

```bash
# Activate virtual environment (macOS/Linux)
source .venv/bin/activate

# Or on Windows:
# .venv\Scripts\activate

# Set environment variable (requires NVIDIA API key)
export NVIDIA_API_KEY="your-api-key"

# Run the example notebook
jupyterlab test_code.ipynb
```

## API Keys Required

- **NVIDIA API Key**: Required for all NVIDIA model operations

## Development

1. Ensure the virtual environment is activated
2. Configure environment variables:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your NVIDIA API key
3. Modify `test_code.ipynb` for your use case
4. Add your documents to the `data/` directory
5. Run the notebook to test your setup

## pyproject.toml

```toml
[project]
name = "ai-engineering"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "jupyterlab>=4.5.8",
    "langchain>=1.3.4",
    "langchain-nvidia-ai-endpoints>=1.4.1",
    "langchain-nvidia-langgraph @ git+https://github.com/langchain-ai/langchain-nvidia.git@main#subdirectory=libs/langgraph",
    "llama-index-core>=0.14.3,<0.15",
    "llama-index-embeddings-nvidia>=0.5.1,<0.6",
    "llama-index-llms-nvidia>=0.5.0,<0.6",
    "llama-index-multi-modal-llms-nvidia>=0.5.2,<0.6",
    "python-dotenv>=1.2.2",
]
```
