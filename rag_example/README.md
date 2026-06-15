# RAG Example

A complete Retrieval Augmented Generation (RAG) implementation using LangChain and Llama Index with NVIDIA AI models.

## Overview

This example demonstrates a real-world RAG pipeline for analyzing project documentation. The RAG system:

1. Loads documents from the `/rag_example/data/` directory
2. Chunks text into manageable pieces for embedding
3. Creates embeddings using NVIDIA's embedding model
4. Stores embeddings in a vector index
5. Answers queries by retrieving relevant document chunks

## Features

- **Complete RAG Pipeline**: Document loading → chunking → embedding → indexing → query answering
- **Smart Chunking**: Uses `TokenTextSplitter` to keep chunks under the 512-token embedding limit
- **Vector Search**: Uses `VectorStoreIndex` for efficient similarity search
- **Configurable Query Engine**: Adjustable top-k retrieval and response format
- **Accuracy Testing**: Automated test suite to validate RAG responses

## Quick Start

```bash
# Navigate to the RAG example directory
cd rag_example

# Run the example notebook
jupyterlab rag_example.ipynb
```

## Prerequisites

- NVIDIA API key (configured in `.env` file)
- Python >= 3.13
- Dependencies installed via `uv sync --active`

## Project Data

The RAG example uses the following data files in `/rag_example/data/`:

| File | Description |
|------|-------------|
| `file1.txt` | Project overview and features |
| `file2.txt` | Setup and dependencies information |
| `file3.txt` | Pipeline architecture and workflow |
| `file4.txt` | Example questions and expected answers |
| `file5.txt` | Indexing and embedding configuration |
| `file6.txt` | Accuracy testing and evaluation |
| `file6.txt` | Troubleshooting common issues |

**Note**: The parent directory `data/file1.txt` is located in the `/core/data/` folder and provides general AI engineering context.

## Usage Example

```python
from dotenv import load_dotenv
from llama_index.llms.nvidia import NVIDIA
from llama_index.embeddings.nvidia import NVIDIAEmbedding
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.text_splitter import TokenTextSplitter

# Load environment variables
load_dotenv()

# Initialize LLM and embedder
llm = NVIDIA(model="openai/gpt-oss-120b")
embedder = NVIDIAEmbedding(model="nvidia/nv-embedqa-e5-v5")
Settings.llm = llm
Settings.embed_model = embedder

# Load documents from RAG data
docs = SimpleDirectoryReader("rag_example/data").load_data()

# Split into chunks (under 512 token limit)
text_splitter = TokenTextSplitter(chunk_size=150, chunk_overlap=30)
nodes = text_splitter.get_nodes_from_documents(docs)

# Build the RAG pipeline
index = VectorStoreIndex(nodes, embed_model=embedder)
query_engine = index.as_query_engine(similarity_top_k=7, response_mode="compact")

# Query the RAG system
response = query_engine.query("How do I implement a RAG system?")
print(response)
```

## Configuration

### Chunking Strategy

NVIDIA's `nv-embedqa-e5-v5` model has a 512-token limit. To avoid errors:

```python
text_splitter = TokenTextSplitter(
    chunk_size=150,      # Keep under 512 token limit
    chunk_overlap=30     # Preserve context between chunks
)
```

### Query Engine

```python
query_engine = index.as_query_engine(
    similarity_top_k=7,  # Return 7 most relevant chunks
    response_mode="compact"  # Compact response format
)
```

## Running Tests

```bash
# Run accuracy tests from the RAG example directory
cd rag_example
python rag_accuracy_test.py
```

The test suite validates:
1. Response quality against expected keywords
2. Retrieved nodes contain relevant information
3. Overall RAG system accuracy

## Troubleshooting

### "Input length exceeds maximum token size 512"

**Cause**: Documents are being split into chunks that are too large.

**Solution**: Reduce `chunk_size` to 150 or less.

### Missing packages

**Solution**: Run `uv sync --active` in the virtual environment.

### Poor response relevance

**Solutions**:
- Use more specific, project-related questions
- Increase `similarity_top_k` value
- Review retrieved nodes for relevance

### API key errors

**Solution**: Ensure `NVIDIA_API_KEY` is set in the `.env` file.

## Project Structure

```
rag_example/
├── data/
│   ├── file1.txt          # Setup and dependencies
│   ├── file2.txt          # Pipeline and architecture
│   ├── file3.txt          # Indexing and embedding details
│   ├── file4.txt          # Example questions and expected answers
│   ├── file5.txt          # Accuracy and evaluation
│   └── file6.txt          # Troubleshooting
├── rag_example.ipynb      # Main RAG implementation
└── rag_accuracy_test.py   # Accuracy test suite
```

## Contributing

Feel free to add your own data files to the `/rag_example/data/` directory or enhance the example notebook with additional queries.

## Related

- Parent repository: [AI Engineering](../README.md) - Core AI engineering patterns and examples
