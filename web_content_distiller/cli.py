"""Command line interface for web-content-distiller."""
from .distiller import distill_html

def main():
    sample = "<html><head><style>body{color:red;}</style></head><body><nav>Menu</nav><h1>Title</h1><p>Article body.</p></body></html>"
    print("Distilled Markdown:
", distill_html(sample))

if __name__ == "__main__":
    main()
