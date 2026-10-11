# AI Engineering Journal

| Date | Task | Prompt | AI output summary | Human validation / changes | Decision | Commit |
|------|------|--------|-------------------|----------------------------|----------|--------|
| 12-10-2026 | Code generation | Build calculate_cgpa, get_cgpa_category and get_student_report with validation, constants, type hints, docstrings | Three functions with a validation helper and named constants | Checked 73 / 9 = 8.11 by hand, ran demo.py, tested boundaries, ran Black and Ruff | Accepted |9964971 |
| 12-10-2026 | Code explanation | Explain calculate_cgpa step by step and list unhandled edge cases | (summarise what Copilot said in one sentence) | (what you compared or tested, and which edge case you noted for future work) | Accepted |hash   |
| 12-10-2026 | Test generation | Write pytest tests for the three functions | Copilot used letter grades (A+, B-, D, F) that do not exist in my code; 16 of 25 tests failed | Compared the tests with my code, replaced the expected values with the real categories, used exact 8.11 instead of loose approx, re-ran pytest, all 19 passed | Modified | ad180b5 |
