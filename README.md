<div align="center">
  <h3>AI Engineering</h3>
  <p>
    <strong>Patterns, tools, and examples for building modern AI applications</strong>
  </p>
  <div style="display: flex; gap: 1rem; justify-content: center; margin: 1rem 0;">
    <img src="https://img.shields.io/badge/python-3.13+-blue?style=for-the-badge&logo=python" alt="Python 3.13+" />
    <img src="https://img.shields.io/badge/langchain-latest-green?style=for-the-badge&logo=langchain" alt="LangChain" />
    <img src="https://img.shields.io/badge/llama_index-latest-blue?style=for-the-badge&logo=meta" alt="LlamaIndex" />
    <img src="https://img.shields.io/badge/nvidia%20ai%20endpoints-latest-orange?style=for-the-badge&logo=nvidia" alt="NVIDIA AI Endpoints" />
    <img src="https://img.shields.io/badge/license-MIT-blue?style=for-the-badge&logo=freedom" alt="MIT License" />
  </div>
</div>

---

## 📖 What is AI Engineering?

This repository is a collection of **patterns, tools, and examples** for building and deploying production-ready AI applications.

Focus areas include:
- **LLM Integration**: Working with LLMs via LangChain and LlamaIndex
- **RAG Pipelines**: Retrieval Augmented Generation architectures
- **Evaluation**: Testing and validating AI app behavior
- **Observability**: Monitoring AI app performance and usage

---

## 🏗️ Repository Structure

```
AI Engineering/
├── rag_example/                  # RAG example
│   ├── data/                    # Example data for testing RAG
│   ├── rag_example.ipynb        # Interactive RAG notebook
│   ├── rag_accuracy_test.py     # RAG evaluation tests
│   └── README.md                # Example documentation
├── pyproject.toml               # Project configuration
├── .env                         # Environment variables (see .env.example)
├── .gitignore                   # Git ignore patterns
└── README.md                    # This file
```

### 📁 Adding New Examples

New examples can be added as subfolders:

```
examples/
├── rag_example/                 # RAG example
├── chatbot/                    # Chat application
├── classification/             # Classification tasks
├── agent/                      # Agentic workflows
└── your_new_example/           # Add your own example!
```

Each example should include:
- `README.md` — Usage documentation
- `*.ipynb` — Interactive notebook
- `test_*.py` — Test suite
- `data/` — Example data files (optional)

---

## 🚀 Quick Start

### Prerequisites

- Python >= 3.13
- [uv](https://github.com/astral-sh/uv) — Fast Python package manager

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd "AI Engineering"

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv sync

# Configure environment
cp .env.example .env
# Edit .env and add your NVIDIA API key
```

### Run Examples

```bash
# Launch JupyterLab with all notebooks
jupyter lab

# Or run specific examples from CLI
python -m your_example
```

---

## 📚 Key Features

### 🔬 Current Examples

| Example | Description |
|---------|-------------|
| `/rag_example` | Complete RAG pipeline with NVIDIA models, chunking, embedding, and evaluation |

### 📦 Stack

- **LangChain** — Modular LLM orchestration framework
- **LlamaIndex** — Data frameworks for LLMs
- **NVIDIA AI Endpoints** — High-performance inference
- **JupyterLab** — Interactive development environment
- **pytest** — Test and validation

---

## 🔑 API Keys Required

| Service | Required | Purpose |
|---------|---------|---------|
| NVIDIA | ✅ | All model inference operations |

### Configuration

Edit the `.env` file:

```bash
NVIDIA_API_KEY="your-api-key-here"
```

---

## 🛠️ Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest rag_accuracy_test.py -v
```

### Linting & Type Checking

```bash
# Format code
uv run ruff format

# Lint
uv run ruff check

# Type check
uv run mypy
```

### Contributing Guide

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone <your-fork-url>
   ```
3. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make changes** and test locally
5. **Commit** with clear messages:
   ```bash
   git commit -m "Add: <description>"
   ```
6. **Push** to GitHub:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

---

## 📝 Guidelines for New Examples

When contributing a new example:

- **[ ]** Document prerequisites and setup
- **[ ]** Include a working notebook or script
- **[ ]** Add unit tests for core functionality
- **[ ]** Include example input/output data
- **[ ]** Write usage documentation
- **[ ]** Ensure tests pass in CI

---

## 🐛 Issues & Questions

Found a bug or have a question? [Open an issue](https://github.com/abhi2020-ds/AI-Engineering/issues) on GitHub.

## 📄 License

MIT License — See [LICENSE.md](LICENSE.md) for details.
