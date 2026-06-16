# TraceAI

A RAG pipeline built from scratch — upload a PDF, ask questions in plain English, get answers traced back to their source. No hallucination.

> Built by Aryan Burman · PES University Bengaluru

## Live Demo
https://rag-doc-qa-aryan.onrender.com/app

---

## What it does

- Upload any PDF and extract its text
- Split text into overlapping chunks for accurate retrieval
- Convert chunks into vector embeddings using Google Gemini
- Store embeddings in a FAISS vector database
- Ask a question — FAISS finds the most relevant chunks
- Gemini generates a grounded answer with source citations

---

## Tech Stack

- **Backend** — FastAPI
- **PDF Parsing** — PyMuPDF
- **Chunking** — LangChain
- **Embeddings + LLM** — Google Gemini
- **Vector Store** — FAISS
- **Frontend** — HTML / Vanilla JS
- **Deployment** — Render

---

## Run Locally

```bash
git clone https://github.com/Aryan-20-2006/traceai.git
cd traceai/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Visit `http://127.0.0.1:8000/app`

---

## Environment Variables

Create a `.env` file in `backend/`:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

Never commit your `.env` file.
