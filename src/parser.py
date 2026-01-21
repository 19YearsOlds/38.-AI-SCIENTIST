import re
from typing import Dict

SECTION_HEADINGS = [
    r"abstract",
    r"introduction",
    r"methods?",
    r"materials and methods",
    r"results?",
    r"discussion",
    r"conclusion"
]

def split_sections(text: str) -> Dict[str, str]:
    """
    Very simple regex-based section splitter.
    Returns dict heading -> text.
    """
    t = text.lower()

    lines = text.splitlines()
    indices = []
    for i, L in enumerate(lines):
        s = L.strip().lower()
        if any(re.match(fr"^{h}\b", s) for h in SECTION_HEADINGS):
            indices.append((i, L.strip()))

    if not indices:
        return {"body": text[:5000]}
    sections = {}
    for idx, (line_no, heading) in enumerate(indices):
        start = line_no
        end = indices[idx + 1][0] if idx + 1 < len(indices) else len(lines)
        sections[heading.lower()] = content
    return sections