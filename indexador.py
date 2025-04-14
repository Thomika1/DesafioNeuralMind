from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings

# Carrega o TXT
loader = TextLoader("data/Procuradoria Geral - Normas.txt", encoding="utf-8")
docs = loader.load()

# Split dos documentos
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", " ", ""]
)
chunks = text_splitter.split_documents(docs)

# Criação dos embeddings
embedding = FastEmbedEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Armazenamento no Chroma
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="./chroma_db"
)

# Salva no disco
vectorstore.persist()
print("✅ TXT indexado com sucesso!")
