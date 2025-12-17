import fitz  # PyMuPDF

def load_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")

    pages = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        if text.strip():
            pages.append({
                "page": page_num,
                "text": text
            })

    return pages
