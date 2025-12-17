import re

def chunk_text(pages, chunk_size=500):
    chunks = []

    for page in pages:
        sentences = re.split(r'(?<=[.!?])\s+', page["text"])
        current_chunk = ""

        for sentence in sentences:
            if len(current_chunk) + len(sentence) <= chunk_size:
                current_chunk += " " + sentence
            else:
                chunks.append({
                    "text": current_chunk.strip(),
                    "page": page["page"]
                })
                current_chunk = sentence

        if current_chunk.strip():
            chunks.append({
                "text": current_chunk.strip(),
                "page": page["page"]
            })

    return chunks
