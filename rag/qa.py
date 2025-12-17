import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=os.getenv("HF_API_TOKEN")
)

def generate_answer(question, context_chunks):
    # Extract only text from retrieved chunks
    context = "\n\n".join(
        chunk["text"] for chunk in context_chunks if "text" in chunk
    )

    prompt = f"""
You are an assistant answering questions strictly from the provided document context.

Rules:
- Use ONLY the context below.
- If the answer is not present, say "I don't know based on the document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.1
    )

    return response.choices[0].message.content.strip()

