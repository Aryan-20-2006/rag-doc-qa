# RAG Document Q&A Engine

Upload a PDF, ask questions in plain English, get answers pulled directly from the document. No hallucination — if the answer isn't in the doc, it says so.

> Built by Aryan · PES University Bengaluru · SDE Internship Portfolio Project

---

## Tech Stack
FastAPI · PyMuPDF · LangChain · FAISS · Google Gemini · HTML/JS

## Status
- [x] FastAPI server + file upload
- [x] PDF text extraction
- [x] Text chunking
- [x] Embeddings + FAISS vector store
- [X] /ask endpoint
- [ ] Frontend
- [ ] Deployment

## Run Locally
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
Visit `http://127.0.0.1:8000/docs` to test.

## Environment Variables
Create a `.env` file in the `backend/` folder:
