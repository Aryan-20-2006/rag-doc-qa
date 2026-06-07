from fastapi import FastAPI, UploadFile, File
import fitz #pymupdf

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
    
    
    return{
        "filename":file.filename,
        "pages":pdf.page_count,
        "text_preview":text[:500],
        "full_text":text
    }