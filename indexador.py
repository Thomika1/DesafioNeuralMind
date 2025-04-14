from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter  # Import correto
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings

# Carrega o PDF
loader = PyPDFLoader("data/Procuradoria Geral - Normas.pdf")
docs = loader.load()

# Configura o splitter corretamente
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", " ", ""]  # Adicione separadores opcionais
)

# Divide os documentos
chunks = text_splitter.split_documents(docs)

# Cria os embeddings
embedding = FastEmbedEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Armazena no ChromaDB
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="./chroma_db"
)

# Persiste os dados (correção de typo)
vectorstore.persist()  
print("✅ Documentos indexados com sucesso!")