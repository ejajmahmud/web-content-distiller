"""Zero-dependency HTML to clean Markdown distiller."""
import re

def distill_html(html: str) -> str:
    # Remove scripts and styles
    clean = re.sub(r"<(script|style|nav|footer)[^>]*>.*?</\1>", "", html, flags=re.DOTALL | re.IGNORECASE)
    # Headings
    clean = re.sub(r"<h1[^>]*>(.*?)</h1>", r"# \1\n\n", clean, flags=re.DOTALL | re.IGNORECASE)
    clean = re.sub(r"<h2[^>]*>(.*?)</h2>", r"## \1\n\n", clean, flags=re.DOTALL | re.IGNORECASE)
    clean = re.sub(r"<h3[^>]*>(.*?)</h3>", r"### \1\n\n", clean, flags=re.DOTALL | re.IGNORECASE)
    # Paragraphs
    clean = re.sub(r"<p[^>]*>(.*?)</p>", r"\1\n\n", clean, flags=re.DOTALL | re.IGNORECASE)
    # Strip remaining tags
    clean = re.sub(r"<[^>]+>", " ", clean)
    # Collapse multiple whitespaces
    clean = re.sub(r"[ \t]+", " ", clean)
    clean = re.sub(r"\n{3,}", "\n\n", clean)
    return clean.strip()
