# Skill: Ultimate AI Engineer (SOP-01)

## Metadata
- **Name:** Ultimate AI Engineer Workflow
- **Triggers:** Mentions of architecture, app building, debugging, refactoring, or code generation.
- **Environment:** Production-grade software engineering (Full-Stack / DevOps / Data Engineering).

## Core Directives
1. **Never skip the planning phase:** Do not write code until a plan is approved.
2. **Maximize Token Efficiency:** Do not write boilerplate; use placeholders `// ... existing code ...` when modifying large files.
3. **Fail Fast:** Write tests concurrently with code changes.
4. **Link references:** Explicitly tag issues, PRs, and absolute file paths in all summaries.

---

## Available Commands

### /plan - Phased Architecture & Execution
When the user requests a feature, fix, or system architecture, execute these steps sequentially:
1. **Analyze:** Inspect existing repository files, schemas, and dependencies.
2. **Design:** Outline the system architecture, API schemas, and data flow.
3. **Breakdown:** Create a checklist of small, atomic, and testable implementation phases.
4. **Halt:** Stop and wait for user approval before writing any code.

### /work - Execution Mode
Execute the approved plan silently with maximum efficiency:
1. Run all code generation in the background.
2. Group related changes into logical files.
3. Add inline comments explaining *why* complex logic was chosen, not *what* it does.
4. Immediately follow up with minimal, highly relevant terminal logs or test execution results.

### /review - Multi-Layer Code Quality Audit
Perform an automated code review on current working changes against these strict pillars:
- **Security:** Check for hardcoded secrets, SQL injection, XSS, and unhandled CORS.
- **Performance:** Look for $O(N^2)$ loops, missing database indexes, and un-memoized UI renders.
- **Clean Code:** Enforce DRY principles, proper naming conventions, and function line limits (<50 lines).
- **Format:** Present findings in a clear table: | File | Line | Issue | Severity (High/Med/Low) | Suggested Fix |.

### /context - Session Handover & Memory Save
When a task is completed, or when preparing to close/reset the session context:
1. Update a project-root `MEMORY.md` file capturing architectural updates and environment changes.
2. Generate a structured git commit message following Conventional Commits format.
3. List remaining technical debt or next-action steps for the next AI session.

---

## Output Layout Templates

### Template: Architecture Plan
```markdown
### 🏗️ Proposed Architecture
- **Impacted Components:** [e.g., `src/components/`, `backend/api/`]
- **Database Migrations:** [Yes/No - include schema changes if Yes]

### 📝 Step-by-Step Implementation Checklist
- [ ] **Phase 1: Foundation** - [Description]
- [ ] **Phase 2: Core Logic** - [Description]
- [ ] **Phase 3: Integration & Testing** - [Description]

*Reply with "Approved" or provide feedback to modify.*
```

### Template: Review Summary
```markdown
### 🔍 Code Review Report

| File | Line | Issue | Severity | Suggested Fix |
| :--- | :--- | :---- | :------- | :------------ |
|      |      |       |          |               |

### 🚀 Recommended Refactor
```python
# Insert clean code snippet here
```
```

---

## Error & Debugging Protocol
If a command, script, or build fails during execution:
1. Do not repeatedly run the same failing command.
2. Read the full stack trace, capture the explicit error boundary, and locate the precise file and line number.
3. Propose exactly **three** distinct hypotheses for why the failure happened.
4. Fix the most likely cause, run the validation script again, and report the delta.

---

## LLM-Specific Guidelines (AI Engineering Project Context)

### Working with LlamaIndex & NVIDIA Models

1. **Always use `settings.llm` and `settings.embed_model`:**
   ```python
   from llama_index.core import Settings
   llm = NVIDIA(model="openai/gpt-oss-120b")
   embedder = NVIDIAEmbedding(model="nvidia/nv-embedqa-e5-v5")
   Settings.llm = llm
   Settings.embed_model = embedder
   ```

2. **Always chunk documents before creating VectorStoreIndex:**
   NVIDIA's embedqa-e5-v5 has a 512 token limit.
   ```python
   from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
   from llama_index.core.text_splitter import TokenTextSplitter

   documents = SimpleDirectoryReader("data").load_data()
   text_splitter = TokenTextSplitter(
       chunk_size=600,
       chunk_overlap=50
   )
   chunks = text_splitter.split_documents(documents)

   index = VectorStoreIndex.from_documents(chunks, embed_model=embedder)
   ```

3. **Recommended models:**
   - LLM: `openai/gpt-oss-120b` or `meta/llama-3.1-70b`
   - Embeddings: `nvidia/nv-embedqa-e5-v5`

4. **Token approximation for Llama 3:** ~1.5 characters per token

---

## Project-Specific Files

- `README.md` - Project documentation
- `pyproject.toml` - Project configuration and dependencies
- `data/*.txt` - Document files for RAG pipeline
- `*.ipynb` - Jupyter notebooks for interactive development
- `.env` - Environment variables (NVIDIA_API_KEY required)

---

## Quick Command Reference

```bash
# Activate environment
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate  # Windows

# Run notebooks
jupyterlab *.ipynb

# Install dependencies
uv sync -v

# Run tests
uv run pytest -v
```
