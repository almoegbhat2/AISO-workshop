import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlparse, parse_qs


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def _clean_duckduckgo_link(link: str) -> str:
    if not link:
        return ""
    if link.startswith("//"):
        return "https:" + link
    if "duckduckgo.com/l/" in link:
        parsed = urlparse(link)
        qs = parse_qs(parsed.query)
        if "uddg" in qs and qs["uddg"]:
            return unquote(qs["uddg"][0])
    return link


def web_search(query: str) -> str:
    """
    Search the web for information.

    Use this tool when a question refers to documentation, changelogs,
    research papers, libraries, or other information that may be online.

    Args:
        query: The search query.

    Returns:
        A short list of search result titles and URLs.
    """
    try:
        url = "https://duckduckgo.com/html/"
        r = requests.get(url, params={"q": query}, headers=HEADERS, timeout=15)
        r.raise_for_status()

        soup = BeautifulSoup(r.text, "html.parser")
        results = []

        for a in soup.select("a.result__a")[:8]:
            title = a.get_text(" ", strip=True)
            link = _clean_duckduckgo_link(a.get("href", ""))
            if title and link:
                results.append(f"{title} - {link}")

        return "\n".join(results) if results else "No results found."
    except Exception as e:
        return f"Web search failed: {str(e)}"


def open_webpage(url: str) -> str:
    """
    Fetch and extract readable text from a webpage.

    Use this tool when a question depends on the content of a webpage.

    Args:
        url: URL of the webpage.

    Returns:
        Cleaned page text.
    """
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        r.raise_for_status()

        soup = BeautifulSoup(r.text, "html.parser")

        for tag in soup(["script", "style", "noscript", "svg", "footer", "nav", "header", "aside"]):
            tag.decompose()

        main = soup.find("main") or soup.find("article")
        target = main if main else soup

        text = target.get_text(separator="\n")
        lines = [line.strip() for line in text.splitlines() if line.strip()]

        seen = set()
        cleaned = []
        for line in lines:
            if line not in seen:
                seen.add(line)
                cleaned.append(line)

        return "\n".join(cleaned[:500])
    except Exception as e:
        return f"Open webpage failed: {str(e)}"


def open_doi(doi: str) -> str:
    """
    Resolve a DOI and extract readable text from the destination page.

    Use this tool when a question gives a DOI or refers to a specific book,
    paper, or chapter identified by DOI.

    Args:
        doi: DOI string, for example '10.1353/book.24372'.

    Returns:
        Cleaned text from the resolved DOI page, including the final URL.
    """
    try:
        doi = doi.strip()
        doi_url = f"https://doi.org/{doi}"

        r = requests.get(
            doi_url,
            headers={**HEADERS, "Accept": "text/html,application/xhtml+xml"},
            timeout=20,
            allow_redirects=True,
        )
        r.raise_for_status()

        final_url = r.url
        soup = BeautifulSoup(r.text, "html.parser")

        for tag in soup(["script", "style", "noscript", "svg", "footer", "nav", "header", "aside"]):
            tag.decompose()

        main = soup.find("main") or soup.find("article")
        target = main if main else soup

        text = target.get_text(separator="\n")
        lines = [line.strip() for line in text.splitlines() if line.strip()]

        seen = set()
        cleaned = []
        for line in lines:
            if line not in seen:
                seen.add(line)
                cleaned.append(line)

        body = "\n".join(cleaned[:500])
        return f"Resolved URL: {final_url}\n\n{body}"
    except Exception as e:
        return f"Open DOI failed: {str(e)}"