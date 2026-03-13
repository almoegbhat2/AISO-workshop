from pathlib import Path
from pypdf import PdfReader

def read_pdf(file_path: str) -> str:
    """
    Read a PDF file and return all extracted text.

    Use this tool when the question depends on the contents of an attached PDF.
    Input:
        file_path: Path to the PDF file.
    Returns:
        Extracted text from all pages as a single string.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    reader = PdfReader(str(path))
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        pages.append(f"\n--- Page {i + 1} ---\n{text}")
    return "\n".join(pages)