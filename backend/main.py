from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import fitz
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings.base import Embeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from google import genai
from dotenv import load_dotenv
import os
from typing import List

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiEmbeddings(Embeddings):
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        result = client.models.embed_content(
            model="models/gemini-embedding-001",
            contents=texts
        )
        return [e.values for e in result.embeddings]

    def embed_query(self, text: str) -> List[float]:
        result = client.models.embed_content(
            model="models/gemini-embedding-001",
            contents=[text]
        )
        return result.embeddings[0].values
    
class Question(BaseModel):
    question: str

app = FastAPI()
embeddings_model = GeminiEmbeddings()
llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

@app.get("/")
def root():
    return {"message": "RAG backend is running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    pdf = fitz.open(stream=contents, filetype="pdf")
    
    text = ""
    for page in pdf:
        text += page.get_text()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_text(text)

    vectorstore = FAISS.from_texts(chunks, embeddings_model)
    vectorstore.save_local("faiss_index")

    return {
        "filename": file.filename,
        "pages": pdf.page_count,
        "total_chunks": len(chunks),
        "message": "Document embedded and indexed successfully"
    }
    
@app.post("/ask")
async def ask_question(body: Question):
    if not os.path.exists("faiss_index"):
        return {"error": "No document uploaded yet. Please upload a PDF first."}

    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings_model,
        allow_dangerous_deserialization=True
    )

    docs = vectorstore.similarity_search(body.question, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""You are a helpful assistant. Answer the question using only the context below.
If the answer is not in the context, say "I couldn't find that in the document."

Context:
{context}

Question: {body.question}

Answer:"""

    response = llm.invoke(prompt)

    return {
        "question": body.question,
        "answer": response.content,
        "source_chunks": [doc.page_content for doc in docs]
    }