from fastapi import FastAPI, UploadFile, File
import fitz #pymupdf
from langchain_text_splitters import RecursiveCharacterTextSplitter



app=FastAPI()

@app.get("/")
def root():
    return {"message":"RAG backend is running"}

@app.post("/upload")
async def upload_file(file:UploadFile=File(...)):
    
    contents=await file.read()
    pdf=fitz.open(stream=contents, filetype='pdf')
    
    text=""
    for page in pdf:
        text+=page.get_text()
        
        
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    
    chunks=splitter.split_text(text)
    
    
    return{
        "filename":file.filename,
        "pages":pdf.page_count,
        "total_chunks":len(chunks),
        "preview":chunks[:3]
        }