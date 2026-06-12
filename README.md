# RAG Document Q&A Engine

Upload a PDF, ask questions in plain English, get answers pulled directly from the document. No hallucination — if the answer isn't in the doc, it says so.

> Built by Aryan Burman · PES University Bengaluru · SDE Internship Portfolio Project

## Live Demo
https://rag-doc-qa-aryan.onrender.com/app

---

## Tech Stack
FastAPI · PyMuPDF · LangChain · FAISS · Google Gemini · HTML/JS

---

## How it works

```
User uploads a PDF
        ↓
FastAPI extracts text using PyMuPDF
        ↓
LangChain splits text into overlapping chunks
        ↓
Google Gemini converts chunks into embeddings
        ↓
Embeddings stored in a FAISS vector database
        ↓
User asks a question
        ↓
FAISS finds the most relevant chunks
        ↓
Gemini generates a grounded answer from those chunks
```

---

## Run Locally

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Visit `http://127.0.0.1:8000/app` to use the app locally.

---

## Environment Variables

Create a `.env` file in the `backend/` folder:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

Never commit your `.env` file.


---

## Author

**Aryan Burman** — CS Engineer & Game Developer  
PES University Electronic City, Bengaluru  
[GitHub](https://github.com/Aryan-20-2006)
