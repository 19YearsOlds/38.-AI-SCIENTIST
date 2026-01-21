import re
from pathlib import Path
import requests
from pypdf import PdfReader
from bs4 import BeautifulSoup
from typing import Dict, Optional

def load_pdf_text(path: Path) -> str:
    """Extract raw text from a PDF file."""
    reader = PdfReader(str(path))
    pages = []
    for pg in reader.pages:
        text = pg.extract_text() or ""
        pages.append(text)
    return "\n".join(pages)

def list_papers(paper_dir: Path):
    return sorted([p for p in papers_dir.glob("*.pdf")])

def fetch_arxiv_metadata(arxiv_id: str) -> Optional[Dict]:
    """Fetch simple metadata from arXiv HTML page (no API here)."""
    url = f"https://export.arxiv.org/api/query?id_list={arxiv_id}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return None
        
        soup = BeautifulSoup(r.text, "xml")
        entry = soup.find("entry")
        if not entry:
            return None
        return {
            "title": entry.title.string.strip(),
            "summary": entry.summary.string.strip(),
            "authors": [a.find("name").string for a in entry.find_all("author")],
            "updated": entry.updated.string,
        }
    except Exception:
        return None