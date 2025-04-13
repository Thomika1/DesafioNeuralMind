__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import sqlite3
sqlite3.sqlite_version  # Força a verificação

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings
import streamlit as st 



load_dotenv()

# Carrega o modelo LLM da Groq
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY") or st.secrets["GROQ_API_KEY"] ,
    model_name="llama3-70b-8192"
)

# Exemplo de vetor store (você pode adaptar com documentos reais)
embedding = FastEmbedEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embedding)
retriever = vectorstore.as_retriever()

# Pipeline básica com prompt
def get_answer(user_input):
    docs = retriever.get_relevant_documents(user_input)
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = ChatPromptTemplate.from_template("""
    Você é um assistente que irá responder perguntas e dúvidas sobre o vestibular da unicamp 2025 com base nos arquivos de normas da procuradoria 
    geral Resolução GR-029/2024, de 10/07/2024.

    Contexto:
    {context}

    Pergunta:
    {question}
    """)

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"context": context, "question": user_input})