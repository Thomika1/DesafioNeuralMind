import streamlit as st
from rag_chain import get_answer

st.set_page_config(page_title="Chatbot vestibular Unicamp", layout="centered")
st.title("🧠 Assistente para dúvidas sobre o vestibular Unicamp 2025")

# Caixa de entrada
user_input = st.text_input("Faça uma pergunta sobre seu conteúdo:", "")

# Chat
if user_input:
    with st.spinner("Pensando..."):
        resposta = get_answer(user_input)
    st.markdown("### 💬 Resposta:")
    st.write(resposta)
