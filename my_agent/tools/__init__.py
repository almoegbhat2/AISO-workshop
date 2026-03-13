from .calculator import calculator
from .pdf_reader import read_pdf, search_pdf, filter_pdf_lines, count_pdf_matches
from .web_tools import web_search, open_webpage, open_doi


__all__ = [
    "calculator",
    "read_pdf",
    "search_pdf",
    "filter_pdf_lines",
    "count_pdf_matches",
    "web_search",
    "open_webpage",
    "open_doi",
]