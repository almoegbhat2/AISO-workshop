from pathlib import Path
from pypdf import PdfReader
import re


def _load_pdf_lines(file_path: str) -> list[str]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    reader = PdfReader(str(path))
    lines = []

    for page in reader.pages:
        text = page.extract_text() or ""
        page_lines = [re.sub(r"\s+", " ", line).strip() for line in text.splitlines()]
        lines.extend([line for line in page_lines if line])

    return lines


def _build_chunks(lines: list[str], window: int = 3) -> list[str]:
    chunks = []
    for i in range(len(lines)):
        chunk = " | ".join(lines[i:i + window])
        if chunk:
            chunks.append(chunk)
    return chunks


def _split_terms(text: str) -> list[str]:
    return [term.strip().lower() for term in text.split("|") if term.strip()]


def read_pdf(file_path: str) -> str:
    """
    Read a PDF file and return cleaned extracted text.

    Use this tool when a question depends on the contents of an attached PDF.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Extracted text as a single string.
    """
    lines = _load_pdf_lines(file_path)
    return "\n".join(lines)


def search_pdf(file_path: str, query: str) -> str:
    lines = _load_pdf_lines(file_path)
    q = query.lower().strip()
    matches = []

    for i, line in enumerate(lines):
        if q in line.lower():
            start = max(0, i - 2)
            end = min(len(lines), i + 3)
            context = "\n".join(lines[start:end])
            matches.append(context)

    # deduplicate
    seen = set()
    unique = []
    for m in matches:
        if m not in seen:
            seen.add(m)
            unique.append(m)

    return "\n\n---\n\n".join(unique[:20]) if unique else "No matches found."

def filter_pdf_lines(file_path: str, include: str, exclude: str = "") -> str:
    """
    Return PDF lines or chunks that contain the include terms and do not contain the exclude terms.

    Use this tool to narrow down relevant entries in PDFs, especially lists, tables,
    catalogs, schedules, or directories.

    Args:
        file_path: Path to the PDF file.
        include: Terms that must appear, separated by | if multiple.
        exclude: Terms that must not appear, separated by | if multiple.

    Returns:
        Matching lines or chunks, or 'No matches found.'
    """
    lines = _load_pdf_lines(file_path)
    chunks = _build_chunks(lines, window=3)

    include_terms = _split_terms(include)
    exclude_terms = _split_terms(exclude)

    def match(text: str) -> bool:
        low = text.lower()
        return all(term in low for term in include_terms) and not any(term in low for term in exclude_terms)

    line_matches = [line for line in lines if match(line)]
    chunk_matches = [chunk for chunk in chunks if match(chunk)]

    results = []
    if line_matches:
        results.append("LINES:\n" + "\n".join(line_matches[:50]))
    if chunk_matches:
        results.append("CHUNKS:\n" + "\n".join(chunk_matches[:50]))

    return "\n\n".join(results) if results else "No matches found."


def count_pdf_matches(file_path: str, include: str, exclude: str = "") -> str:
    lines = _load_pdf_lines(file_path)

    include_terms = _split_terms(include)
    exclude_terms = _split_terms(exclude)

    def match(text: str) -> bool:
        low = text.lower()
        return all(term in low for term in include_terms) and not any(term in low for term in exclude_terms)

    matched_lines = []
    for line in lines:
        if match(line):
            matched_lines.append(line.strip().lower())

    unique_matches = list(dict.fromkeys(matched_lines))
    return str(len(unique_matches))