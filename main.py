import streamlit as st
from rag_chain import get_answer
import time

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

st.set_page_config(
    page_title="Chatbot vestibular Unicamp",
    layout="centered",
    initial_sidebar_state="collapsed" 
)

with st.sidebar:
    st.link_button("📄 Ver Documento Oficial", "https://www.pg.unicamp.br/norma/31879/0")


# Configuração da página
st.title("Assistente virtual vestibular Unicamp 2025")

# Inicializar o histórico de chat
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Olá, qual sua dúvida?"}]

# Exibir mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Caixa de entrada
if prompt := st.chat_input("Digite aqui"):
    
    # Exibir mensagem do usuário
    with st.chat_message("user"):
        st.markdown(prompt)

    # Adicionar mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # inicia o contador de tempo de resposta
    start = time.time()
    # Gerar resposta
    with st.spinner("Pensando..."):
        resposta = get_answer(prompt)
    # Fim do contador de tempo de resposta
    end = time.time()
    # Exibir resposta
    with st.chat_message("assistant"):
        st.caption(f"🕒 Tempo de resposta: {end - start:.2f} segundos")
        st.markdown(resposta)
    # Adicionar resposta ao histórico
    st.session_state.messages.append({"role": "assistant", "content": resposta})
    


