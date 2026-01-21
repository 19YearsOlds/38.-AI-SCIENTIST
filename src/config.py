import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT / "data"
PAPERS_DIR = DATA_DIR / "papers"
DATASETS_DIR = DATA_DIR / "datasets"

OUTPUT_DIR = ROOT / "outputs"
EXP_DIR = OUTPUT_DIR / "experiments"
ANALYSIS_DIR = OUTPUT_DIR / "analyses"


DEFAULT_SEED = 42
DEFAULT_EPOCHS = 20
BATCH_SIZE = 64
LR = 1e-3

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
LLM_MODEL = "gpt-4o-mini"


for p in [PAPERS_DIR, DATASETS_DIR, EXP_DIR, ANALYSIS_DIR]:
    p.mkdir(parents=True, exist_ok=True)