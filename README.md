AI Scientist - mini RAG-style research assistant + experiment simulator.

Quick start:
1. pip install -r requirements.txt
2. Put some PDFs in data/papers/
3. Run: python -m src.runner data/papers/yourpaper.pdf

What it does:
- Extracts sections from PDFs
- Creates a synthetic dataset and runs a simple regression experiment
- Analyzes results and (optionally) calls an LLM to propose hypotheses

Notes:
- The code is intentionally minimal and safe: it simulates computational experiments only.
- If you want real experiment simulation (e.g., molecular dynamics), that requires specialized tools and domain safety checks.