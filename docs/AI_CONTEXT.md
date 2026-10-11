# AI Context: Student Performance Management System

Purpose: manage student marks and compute CGPA (10-point scale, credit weighted).
Language: Python 3.x
Structure: src/ (code), tests/ (pytest), docs/ (documentation, AI journal), config/ (non-secret configuration)

Rules for the AI assistant:
- Follow PEP 8. Code is formatted with Black and linted with Ruff.
- Add type hints and a docstring to every function.
- Every new function must have pytest tests in tests/.
- Never hard-code passwords, API keys or real student data.
- Do not modify files in config/ without human approval.
- Prefer small functions and state any assumptions you make.