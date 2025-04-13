__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import sqlite3
sqlite3.sqlite_version  # Força a verificação
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter as sp
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings as em # ou HuggingFace
from Chroma import Settings

client_settings = Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_db",
    anonymized_telemetry=False
)


# 1. Carrega seu PDF
loader = PyPDFLoader("data/Procuradoria Geral - Normas.pdf")
docs = loader.load()

# 2. Divide em pedaços menores (ex: 500 tokens com 50 de sobreposição)
text_splitter = sp.RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(docs)

# 3. Embeddings
embedding = em.FastEmbedEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 4. Salva no Chroma
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="./chroma_db"
)

vectorstore.persist()
print("✅ Documentos indexados!")
