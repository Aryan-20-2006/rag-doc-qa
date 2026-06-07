# RAG Document Q&A Engine

Upload a PDF, ask questions in plain English, get answers pulled directly from the document. No hallucination — if the answer isn't in the doc, it says so.

> Built by Aryan · PES University Bengaluru · SDE Internship Portfolio Project

---

## Tech Stack
FastAPI · PyMuPDF · LangChain · FAISS · OpenAI GPT-4o-mini · HTML/JS

## Status
- [x] FastAPI server + file upload
- [x] PDF text extraction
- [ ] Text chunking
- [ ] Embeddings + FAISS
- [ ] /ask endpoint
- [ ] Frontend
- [ ] Deployment

## Run Locally
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
Visit `http://localhost:8000/docs` to test.
