import os
from typing import List, Dict, Optional
from . import config

USE_OPENAI = config.OPENAI_API_KEY is not None

if USE_OPENAI:
    import openai
    openai.api_key = config.OPENAI_API_KEY

PROMPT_TEMPLATE = """
You are an AI research assistant. Given the paper excerpts and experimental results below, propose 3 concise, plausible, and testable hypotheses or research directions.

Paper sections:
{paper_sections}

Experimental summary:
{experimental_summary}

Constraints/notes:
- Keep each hypothesis short (1-2 sentences).
- For each hypothesis, add a one-line proposed computational experiment to test it.
"""

def generate_hypotheses(paper_sections: str, experiment_summary: str, n=3) -> List[Dict]:
    prompt = PROMPT_TEMPLATE.format(
        paper_sections=paper_sections[:4000],
        experiment_summary=experiment_summary[:2000]
    )
    if USE_OPENAI:
        resp = openai.ChatCompletion.create(
            model=config.LLM_MODEL,
            messages=[{"role":"user", "content": prompt}],
            max_tokens=400
        )
        text = resp["choices"][0]["message"]["content"]
    else:
        text = (
            "1) Hypothesis A: ... (test by running a synthetic regression sweep)\n"
            "2) Hypothesis B: ... (test using ablation of input features)\n"
            "3) Hypothesis C: ... (test by scaling dataset size)\n"
        )

    bullets = [b.strip() for b in text.split("\n") if b.strip()]
    return [{"hypothesis": b} for b in bullets][:n]