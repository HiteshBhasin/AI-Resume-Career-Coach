from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()


def processingFile(text):
    embedding = OpenAIEmbeddings(model ="text-embedding-3-large")
    split_text = RecursiveCharacterTextSplitter(chunk_size =250 , chunk_overlap = 0)
    text_for_agent = split_text.split_text(text)
    # Chroma.from_documents()
    vector_store = Chroma.from_texts(text_for_agent, embedding, collection_name="resume_data")
    return vector_store
    

