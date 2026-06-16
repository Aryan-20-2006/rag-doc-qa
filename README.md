TraceAI

Ask questions about any PDF and get answers sourced directly from the document — with citations, no hallucination. If the answer isn't in the doc, it says so.


Built by Aryan Burman · PES University Bengaluru · SDE Internship Portfolio Project


## Live Demo
https://traceai-aryan.onrender.com/app


How it works

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
        ↓
Answer returned with source citations


What makes it different

Most AI chatbots generate answers from general knowledge — they can hallucinate and you can't verify where the answer came from. TraceAI only answers from your document, and returns the exact source chunks it used to generate the answer. Every response is traceable.


Tech Stack

LayerTechnologyBackend frameworkFastAPIPDF parsingPyMuPDFText chunkingLangChainEmbeddings + LLMGoogle GeminiVector storeFAISSFrontendHTML / Vanilla JSDeploymentRender


Run Locally

bashgit clone https://github.com/Aryan-20-2006/rag-doc-qa.git
cd rag-doc-qa/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000

Visit http://127.0.0.1:8000/app to use the app locally.


Environment Variables

Create a .env file inside the backend/ folder:

GEMINI_API_KEY=your_gemini_api_key_here

Never commit your .env file.


Author

Aryan Burman — CS Engineer & Game Developer

PES University Electronic City, Bengaluru

GitHub
