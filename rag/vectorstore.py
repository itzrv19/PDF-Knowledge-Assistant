import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

COLLECTION_NAME = "pdf_chunks_v1"  # versioned name

def create_vector_store(chunks):
    client = chromadb.Client()

    # Always start clean for this schema version
    try:
        client.delete_collection(COLLECTION_NAME)
    except:
        pass

    collection = client.create_collection(name=COLLECTION_NAME)

    texts = [c["text"] for c in chunks]
    pages = [c["page"] for c in chunks]

    embeddings = model.encode(texts, show_progress_bar=True)

    collection.add(
        documents=texts,
        embeddings=embeddings.tolist(),
        metadatas=[{"page": p} for p in pages],
        ids=[str(i) for i in range(len(texts))]
    )

    return collection


def retrieve_chunks(collection, query, k=4):
    query_embedding = model.encode([query])

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=k
    )

    retrieved = []

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    for i, text in enumerate(documents):
        meta = metadatas[i] if metadatas and metadatas[i] else {}
        page = meta.get("page", "Unknown")

        raw_score = 1 - distances[i] if distances and i < len(distances) else 0.0
        score = round(max(0.0, min(raw_score, 1.0)), 3)

        retrieved.append({
            "text": text,
            "page": page,
            "score": score
        })

    return retrieved
