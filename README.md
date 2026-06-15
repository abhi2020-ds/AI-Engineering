# AI Engineering

A comprehensive repository for learning AI engineering best practices, patterns, and implementation examples. This repository provides a clean structure for exploring and building AI applications using modern tools and frameworks.

## Overview

**AI Engineering** is the core repository containing:
- Core AI engineering patterns and best practices
- Shared utilities and tools
- Evaluation frameworks
- Example implementations

### Quick Start

```bash
# Clone the repository
git clone <repo-url>

# Install dependencies
uv sync --active

# Set NVIDIA API key
export NVIDIA_API_KEY="your-api-key"
```

## Repository Structure

```
AI Engineering/
├── core/                          # Core AI engineering
│   ├── data/                     # Core documentation
│   │   ├── file1.txt             # Project overview & core concepts
│   │   ├── file2.txt             # API design best practices
│   │   ├── file3.txt             # Prompt engineering best practices
│   │   ├── file4.txt             # Model selection guide
│   │   ├── file5.txt             # Error handling strategies
│   │   └── file6.txt             # Token management
│   ├── notebooks/                # Core example notebooks
│   │   └── (add your notebooks here)
│   └── test/                     # Core test suite
│       └── api_test.py           # API and configuration tests
│
├── rag_example/                  # RAG example (subfolder)
│   ├── README.md                 # RAG example documentation
│   ├── rag_example.ipynb         # RAG implementation example
│   ├── rag_accuracy_test.py      # RAG accuracy testing
│   └── data/                    # RAG-specific data files
│       ├── file2.txt            # Setup and dependencies
│       ├── file3.txt            # Pipeline and architecture
│       ├── file4.txt            # Example questions
│       ├── file5.txt            # Indexing and embedding details
│       ├── file6.txt            # Accuracy and evaluation
│       └── file7.txt            # Troubleshooting
│
├── pyproject.toml               # Project configuration
├── uv.lock                      # Locked dependency versions
├── .env                         # Environment variables (API keys)
├── .gitignore                   # Git ignore patterns
└── README.md                    # This file
```

## Getting Started

### Installation

```bash
# Install dependencies
uv sync --active

# Configure environment
cp .env.example .env  # if available
# Or edit .env directly:
NVIDIA_API_KEY=your-api-key
```

### Running Examples

```bash
# Run core examples
jupyterlab core/notebooks/test_code.ipynb

# Or run RAG example
jupyterlab rag_example/rag_example.ipynb
```

## Subfolders

### `/core` - Core AI Engineering

Core AI engineering concepts including:
- **Patterns**: Design patterns, best practices, architectural guidelines
- **Data**: Documentation on core AI concepts
- **Notebooks**: Interactive examples for core concepts
- **Test**: Test suite for validating core implementations

### `/rag_example` - RAG Example

A complete Retrieval Augmented Generation example:
- Demonstrates a full RAG pipeline with NVIDIA models
- Includes chunking, embedding, vector search, and query answering
- Comprehensive test suite with accuracy validation
- RAG-specific data files for testing

## Dependencies

- Python >= 3.13
- [uv](https://github.com/astral-sh/uv) - Fast Python package manager
- [LangChain](https://python.langchain.com/) - Modular LLM framework
- [Llama Index](https://docs.llamaindex.ai/) - LLM application frameworks
- [NVIDIA AI Endpoints](https://github.com/langchain-ai/langchain-nvidia/) - NVIDIA model integrations
- JupyterLab - Interactive development
- python-dotenv - Environment variable management

## API Keys Required

- **NVIDIA API Key**: Required for all NVIDIA model operations

Configure by editing the `.env` file with your NVIDIA API key.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes and test locally
4. Submit a pull request

## License

[Specify your license here]

## Contact

For questions or issues, please open an issue in the repository.
