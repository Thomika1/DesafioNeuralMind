import streamlit as st
from rag_chain import get_answer

# Configuração da página
st.set_page_config(page_title="Chatbot vestibular Unicamp", layout="centered")
st.title("Assistente virtual vestibular Unicamp 2025")

# Inicializar o histórico de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Caixa de entrada
if prompt := st.chat_input("Faça uma pergunta sobre o vestibular Unicamp 2025:"):
    # Adicionar mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Exibir mensagem do usuário
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    
    # Gerar resposta
    with st.spinner("Pensando..."):
        resposta = get_answer(prompt)
    
    # Adicionar resposta ao histórico
    st.session_state.messages.append({"role": "assistant", "content": resposta})
    
    # Exibir resposta
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(resposta)



