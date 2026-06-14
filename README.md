# AI Engineering

A Python-based AI engineering project using LangChain and Llama Index for Retrieval Augmented Generation (RAG). This project provides tools for querying documents and generating responses using NVIDIA's AI models.

## Features

- **RAG Pipeline**: Build retrieval-augmented generation applications using LangChain and Llama Index
- **NVIDIA Models**: Integration with NVIDIA's AI model stack (Llama 3, embeddings, multimodal models)
- **Document Processing**: Load and process documents from directories using SimpleDirectoryReader
- **Text Chunking**: Implement smart text splitting with TokenTextSplitter and RecursiveCharacterTextSplitter
- **Vector Search**: Create and query vector indexes for semantic search
- **Accuracy Testing**: Validate RAG responses with keyword-based matching and retrieval analysis

## Dependencies

- Python >= 3.13
- [LangChain](https://python.langchain.com/) - Modular LLM application framework
- [Llama Index](https://docs.llamaindex.ai/) - Data frameworks for LLM applications
- [NVIDIA AI Endpoints](https://github.com/langchain-ai/langchain-nvidia/) - NVIDIA AI model integrations
- JupyterLab - Interactive development environment
- [uv](https://github.com/astral-sh/uv) - Fast Python package and project manager

## Project Structure

```
AI Engineering/
├── data/                          # Document files for RAG
│   ├── file1.txt                  # Project overview (features)
│   ├── file2.txt                  # Setup and dependencies
│   ├── file3.txt                  # Pipeline and architecture
│   ├── file4.txt                  # Example questions and expected answers
│   ├── file5.txt                  # Indexing and embedding details
│   ├── file6.txt                  # Accuracy and evaluation
│   └── file7.txt                  # Troubleshooting
├── rag_accuracy_test.py           # Automated RAG accuracy testing
├── rag_example.ipynb              # Real-world RAG example (code analysis)
├── test_code.ipynb               # Example notebook with basic usage
├── pyproject.toml                # Python project configuration
├── uv.lock                       # Locked dependency versions
└── README.md                     # This file
```

## Quick Start

```bash
# Clone and install dependencies
uv sync --active

# Activate virtual environment (macOS/Linux)
source .venv/bin/activate

# Set NVIDIA API key in .env file
# Edit .env and add: NVIDIA_API_KEY=your-api-key

# Run the example notebook
jupyterlab rag_example.ipynb
```

## API Keys Required

- **NVIDIA API Key**: Required for all NVIDIA model operations (configured in `.env`)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   uv sync --active
   ```
3. Set environment variables by editing `.env`:
   ```bash
   NVIDIA_API_KEY=your-api-key
   ```
4. Open `rag_example.ipynb` in JupyterLab

## Usage Examples

### Basic RAG Setup

```python
from dotenv import load_dotenv
from llama_index.llms.nvidia import NVIDIA
from llama_index.embeddings.nvidia import NVIDIAEmbedding
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.text_splitter import TokenTextSplitter

# Load environment variables
load_dotenv()

# Initialize LLM with NVIDIA model
llm = NVIDIA(model="openai/gpt-oss-120b")

# Initialize embedding model
embedder = NVIDIAEmbedding(model="nvidia/nv-embedqa-e5-v5")

# Configure settings
Settings.llm = llm
Settings.embed_model = embedder

# Load and chunk documents
documents = SimpleDirectoryReader("data").load_data()

# Split text for smaller chunks (NVIDIA embedqa-e5-v5 has 512 token limit)
text_splitter = TokenTextSplitter(chunk_size=150, chunk_overlap=30)
nodes = text_splitter.get_nodes_from_documents(documents)

# Create vector index and query engine
index = VectorStoreIndex(nodes, embed_model=embedder)
query_engine = index.as_query_engine(similarity_top_k=7, response_mode="compact")

# Query the index
response = query_engine.query("What are the main features of this project?")
print(response)
```

### Advanced Example (Recursive Chunking)

```python
from llama_index.text_splitters import RecursiveCharacterTextSplitter

# Load and chunk documents
documents = SimpleDirectoryReader("data").load_data()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(documents)

# Create index from chunks
index = VectorStoreIndex.from_documents(chunks)
query_engine = index.as_query_engine()

# Query the index
response = query_engine.query("What are the main features of this project?")
print(response)
```

## Running Tests

```bash
# Run RAG accuracy test
python rag_accuracy_test.py
```

## Key Configuration

### Chunking Strategy

Recommended settings for NVIDIA's 512-token embedding limit:

```python
from llama_index.core.text_splitter import TokenTextSplitter

text_splitter = TokenTextSplitter(
    chunk_size=150,      # Keep under 512 token limit
    chunk_overlap=30     # Preserve context between chunks
)
```

### NVIDIA Model Configuration

- **LLM**: `openai/gpt-oss-120b` (via NVIDIA AI Endpoints)
- **Embeddings**: `nvidia/nv-embedqa-e5-v5` (512-token limit)

### Query Engine Settings

```python
query_engine = index.as_query_engine(
    similarity_top_k=7,  # Return top 7 most relevant chunks
    response_mode="compact"  # Compact response format
)
```

## Development

1. Ensure `uv` is installed
2. Run `uv sync --active` to install dependencies
3. Edit `.env` and add your NVIDIA API key:
   ```bash
   NVIDIA_API_KEY=your-api-key
   ```
4. Modify `test_code.ipynb` or `rag_example.ipynb` for your use case
5. Add your documents to the `data/` directory
6. Run the notebook or accuracy test

## Running Tests

```bash
# Run RAG accuracy test to validate responses
python rag_accuracy_test.py
```

## Troubleshooting

### Token Length Exceeded Error

```
Input length exceeds maximum allowed token size 512
```

**Solution**: Reduce chunk size to 150 or 120 and keep chunk_overlap at 30.

### Missing Packages

```bash
# Re-sync dependencies
uv sync --active
```

### Poor Relevance

- Use more specific, project-related questions
- Verify the top retrieved nodes contain relevant content
- Check the accuracy test results for insights

## pyproject.toml

```toml
[project]
name = "ai-engineering"
version = "0.1.0"
description = "AI engineering project with RAG using LangChain and Llama Index"
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

## Examples

- **rag_example.ipynb**: Real-world RAG example for code analysis with comprehensive query testing

## Related Resources

- [RAG Accuracy Test](rag_accuracy_test.py): Automated test to validate RAG responses
- [Project Data Files](data/): Document content for RAG testing
