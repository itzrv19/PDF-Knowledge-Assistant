# 📘 PDF Knowledge Assistant

A chat-based **Retrieval-Augmented Generation (RAG)** application that allows users to ask
questions directly from PDF documents and receive **accurate, document-grounded answers**
with **page-level citations** and **relevance scoring**.

This project is designed with a strong focus on **trust, transparency, and usability**,
ensuring that answers are generated strictly from the uploaded document — without
hallucinations or external knowledge.

---

## 🚀 Features

- 📄 Upload any PDF and interact with its content
- 💬 Chat-style conversational interface
- 📌 Page-level citations for each answer
- 🎯 Relevance scoring with visual indicators
- 🛡️ Strictly document-grounded answers (no hallucinations)
- 🎨 Clean, professional, and intuitive UI
- 🔐 Secure handling of API keys (no hardcoding)

---
---

## 🌐 Live Demo

🔗 **Live Application**

```text
https://your-app-name.streamlit.app
```

---

## 🧠 How It Works

1. **PDF Loading**  
   The uploaded PDF is read page-by-page while preserving page numbers.

2. **Text Chunking**  
   Each page is split into meaningful, sentence-based chunks while keeping metadata
   such as the page number.

3. **Embedding Generation**  
   Each chunk is converted into a semantic vector using a Sentence Transformer model.

4. **Vector Storage**  
   All embeddings are stored in a ChromaDB vector database along with their metadata.

5. **Semantic Retrieval**  
   When a question is asked, the most relevant chunks are retrieved using vector
   similarity search.

6. **Answer Generation**  
   A language model generates answers **strictly from the retrieved chunks**.
   If the answer is not present in the document, the assistant responds accordingly.

7. **Explainability**  
   The UI displays:
   - Page numbers for source content
   - Relevance scores for each retrieved chunk
   - Optional visibility into the supporting text

---

## 🧩 Architecture Overview

```text
PDF Document
     ↓
Page-wise Parsing
     ↓
Sentence Chunking
     ↓
Vector Embeddings
     ↓
ChromaDB Vector Store
     ↓
Semantic Retrieval
     ↓
LLM Answer Generation
     ↓
Chat UI with Citations & Scores



---

## 🛠️ Tech Stack

- **Frontend / UI**: Streamlit
- **Vector Database**: ChromaDB
- **Embeddings**: Sentence Transformers (`all-MiniLM-L6-v2`)
- **LLM Inference**: Hugging Face Inference API
- **PDF Processing**: PyMuPDF
- **Language**: Python

---

## 🔐 Security & Best Practices

- API keys are **never hardcoded**
- Secrets are managed using **environment variables**
- `.env` files are excluded using `.gitignore`
- Deployment secrets are stored using platform secret managers
- Clean separation between UI, retrieval, and generation logic

---

## 📂 Project Structure

rag-pdf-app/
│
├── app.py                # Streamlit application
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Ignore secrets & cache files
│
├── rag/
│   ├── loader.py         # PDF loading with page metadata
│   ├── chunker.py        # Sentence-based text chunking
│   ├── vectorstore.py    # Vector storage & retrieval logic
│   └── qa.py             # Answer generation using LLM



---

## 🧪 Example Use Cases

- Studying from textbooks and research papers
- Quickly finding information in large PDFs
- Verifying answers with exact page references
- Understanding and summarizing technical documents

---

## 🎯 Why This Project Matters

Unlike generic AI chatbots, this assistant:

- Does **not hallucinate**
- Produces **verifiable answers**
- Clearly shows **where each answer comes from**
- Emphasizes **explainable and trustworthy AI**

This project demonstrates a **real-world RAG system** with production-oriented design,
not a prompt-only chatbot or tutorial example.

---

## 📌 Future Enhancements

- Inline citations within generated answers
- Export chat history as PDF
- Support for multiple PDFs
- Highlighting answer sentences in source text
- Deployment on Streamlit Cloud or Hugging Face Spaces

---

## 🧠 Author Notes

This project was built with a focus on **clean architecture, robustness, and user trust**.
It reflects production-level thinking and practical application of
Retrieval-Augmented Generation systems.

---

⭐ If you find this project useful, consider starring the repository!
