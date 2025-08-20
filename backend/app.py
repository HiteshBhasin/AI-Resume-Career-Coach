from __future__ import annotations
from fastapi import FastAPI
from fastapi import File, UploadFile
from pydantic import BaseModel
import asyncio
from pypdf import PdfReader

app = FastAPI()

@app.get("/")
async def indexPage():
    return {"message": "Welcome to my App"}
    

@app.post("/upload")
async def processingFile(resume:UploadFile = File(...)):
    contents = await resume.read()
    resumer_text=extract_from_pdf(contents)
    
    
def extract_from_pdf(pdf_path):
    reader=PdfReader(pdf_path)
    text=""
    for pages in reader.pages:
        text+=pages.extract_text()
    return text
        
    
