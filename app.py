import streamlit as st
from rag.loader import load_pdf
from rag.chunker import chunk_text
from rag.vectorstore import create_vector_store, retrieve_chunks
from rag.qa import generate_answer

# ---------- Page Config ----------
st.set_page_config(
    page_title="PDF Knowledge Assistant",
    layout="centered"
)

# ---------- Session State ----------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "collection" not in st.session_state:
    st.session_state.collection = None

# ---------- Header ----------
st.title("📘 PDF Knowledge Assistant")
st.caption(
    "Chat with your PDF and get clear, document-grounded answers."
)

# ---------- Reset Button ----------
if st.button("🗂️ Start with a new document"):
    st.session_state.chat_history = []
    st.session_state.collection = None
    st.rerun()

st.markdown("---")

# ---------- Upload Section ----------
st.markdown("### 📄 Upload your document")
uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type="pdf",
    label_visibility="collapsed"
)

# ---------- Document Processing ----------
if uploaded_file and st.session_state.collection is None:
    with st.spinner("📄 Reading and understanding the document..."):
        pages = load_pdf(uploaded_file)
        chunks = chunk_text(pages)
        st.session_state.collection = create_vector_store(chunks)

    st.success("Document processed successfully.")
    st.info(f"📘 You are now chatting with **{uploaded_file.name}**")

# ---------- First-time Hint ----------
if uploaded_file and not st.session_state.chat_history:
    st.markdown(
        """
        💡 **Try asking questions like:**
        - What are ....?
        - Explain ....
        - Summarize this ....
        """
    )

# ---------- Question Input ----------
st.markdown("### 💬 Ask a question")
question = st.text_input(
    "Type your question here",
    placeholder="e.g. What are .....?"
)

# ---------- Ask Button ----------
if st.button("🔍 Ask", use_container_width=True):
    if uploaded_file is None:
        st.warning("Please upload a PDF first.")
    elif question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("🔍 Searching relevant sections..."):
            retrieved_chunks = retrieve_chunks(
                st.session_state.collection,
                question,
                k=4
            )

        with st.spinner("✍️ Assistant is composing an answer..."):
            answer = generate_answer(
                question,
                retrieved_chunks
            )

        # Save conversation
        st.session_state.chat_history.append({
            "question": question,
            "answer": answer,
            "sources": retrieved_chunks
        })

        st.rerun()

# ---------- Chat History ----------
if st.session_state.chat_history:
    st.markdown("---")
    st.markdown("## 💬 Conversation")

    for chat in st.session_state.chat_history:
        # User
        st.markdown("**🧑 You:**")
        st.info(chat["question"])

        # Assistant (Premium Answer Box)
        st.markdown(
            f"""
            <div style="
                background-color:#0f5132;
                padding:16px;
                border-radius:10px;
                color:white;
                font-size:16px;
            ">
            <b>Answer</b><br><br>
            {chat["answer"]}
            </div>
            """,
            unsafe_allow_html=True
        )

        # Sources + relevance
        with st.expander("📌 Answer sources & relevance"):
            for i, src in enumerate(chat["sources"]):
                clean_text = " ".join(src["text"].split())

                st.markdown(f"**Source {i+1} — Page {src['page']}**")
                st.progress(max(0.0, min(src["score"], 1.0)))
                st.caption(f"Relevance score: {src['score']}")
                st.text(clean_text[:400])

# ---------- How It Works ----------
with st.expander("🧠 How this assistant works"):
    st.markdown("""
    1. The PDF is split into meaningful sections.
    2. Relevant sections are retrieved based on your question.
    3. Answers are generated strictly from those sections.
    """)

# ---------- Footer ----------
st.markdown("---")
st.caption(
    "🛡️ Answers are generated strictly from the uploaded document. No external knowledge is used."
)
