RAG Document Q&A Engine
A backend AI application that lets you upload any PDF and ask questions about it in plain English. Built with FastAPI, LangChain, FAISS, and OpenAI — a mini version of how Google's AI Overviews work, but for your private documents.

Status: 🚧 In Progress


What it does
Upload a PDF → ask a question → get a grounded answer pulled directly from the document, with source references.
No hallucination. If the answer isn't in the document, it says so.

Tech Stack
LayerTechnologyBackend frameworkFastAPIPDF parsingPyMuPDF (fitz)Text chunkingLangChain RecursiveCharacterTextSplitterEmbeddingsOpenAI text-embedding-ada-002Vector storeFAISSLLMOpenAI GPT-4o-miniFrontendHTML / Vanilla JSDeploymentRender.com

Architecture
User uploads PDF
      ↓
FastAPI /upload endpoint
      ↓
PyMuPDF extracts raw text
      ↓
LangChain splits text into ~500 token chunks
      ↓
OpenAI embeds each chunk → stored in FAISS index
      ↓
User asks a question via /ask endpoint
      ↓
FAISS similarity search → top-k relevant chunks retrieved
      ↓
Chunks + question sent to GPT-4o-mini
      ↓
Grounded answer returned with source references

Project Structure
rag-doc-qa/
├── backend/
│   ├── main.py          # FastAPI app — all endpoints
│   ├── requirements.txt # Python dependencies
│   └── venv/            # Virtual environment (not committed)
├── frontend/
│   └── index.html       # Upload UI + chat interface
├── .env.example         # Environment variable template
├── .gitignore
└── README.md

Getting Started
Prerequisites

Python 3.10+
An OpenAI API key (get one here)

1. Clone the repo
bashgit clone https://github.com/your-username/rag-doc-qa.git
cd rag-doc-qa
2. Set up the virtual environment
bashcd backend
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
3. Install dependencies
bashpip install -r requirements.txt
4. Set up environment variables
bashcp .env.example .env
Open .env and add your OpenAI API key:
OPENAI_API_KEY=your_key_here
5. Run the server
bashuvicorn main:app --reload
Visit http://localhost:8000/docs to test the API interactively.

API Endpoints
MethodEndpointDescriptionGET/Health checkPOST/uploadUpload a PDF and extract + embed textPOST/askAsk a question about the uploaded document
POST /upload
json// Request: multipart/form-data with PDF file

// Response
{
  "filename": "research_paper.pdf",
  "pages": 12,
  "chunks_created": 47,
  "message": "Document processed and indexed successfully"
}
POST /ask
json// Request
{
  "question": "What are the key findings?"
}

// Response
{
  "answer": "The key findings include...",
  "source_chunks": ["chunk text 1", "chunk text 2"]
}

Environment Variables
Create a .env file in the backend/ folder:
OPENAI_API_KEY=your_openai_api_key_here
Never commit your .env file. It's already in .gitignore.

Roadmap

 FastAPI server setup
 PDF upload endpoint
 Text extraction with PyMuPDF
 Text chunking with LangChain
 Embeddings + FAISS vector store
 LLM integration + /ask endpoint
 HTML frontend
 Deployment on Render


What I learned building this

How RAG (Retrieval Augmented Generation) pipelines work end-to-end
Building and deploying REST APIs with FastAPI
Vector embeddings and similarity search with FAISS
Prompt engineering to prevent LLM hallucination
Connecting a vanilla JS frontend to a Python backend


Author
Aryan — 5th Semester CS, PES University Bengaluru
Built as a portfolio project targeting SDE internships.

