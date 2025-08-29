from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

def processingFile(text):
    embedding = OpenAIEmbeddings(model ="text-embedding-3-large")
    split_text = RecursiveCharacterTextSplitter(chunk_size =10 , chunk_overlap = 2)
    text_for_agent = split_text.split_text(text)
    

