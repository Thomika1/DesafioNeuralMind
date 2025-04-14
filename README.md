# Chatbot Vestibular Unicamp 2025

A versão hospedada na nuvem do chat bot pode ser encontrada em: [Link](https://desafionm.streamlit.app/)

Assistente virtual para tirar dúvidas sobre o vestibular da Unicamp 2025, baseado na Resolução GR-029/2024.

## Pré-requisitos

- Python 3.10 ou superior
- Poetry (ou pip)
- Conta na Groq (para API key)

## Como executar localmente

### 1. Clone o repositório
```
git clone https://github.com/Thomika1/DesafioNeuralMind
```

### 2. Configure a variável de ambiente
Crie um arquivo .env na raiz do projeto com:

```
GROQ_API_KEY="sua-chave-groq-aqui"
```
### 3. Instale as dependências
Opção A (com Poetry):
```
poetry install
```
Opção B (com pip):

*Se o terminal usado é alternativo ao padrão do linux (exemplo: fish) o comando para ativar o ambiente virtual pode mudar*
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
```
### 4. Execute o chatbot
```
streamlit run app.py
```
## Tecnologias utilizadas

- Framework: Streamlit
- LLM: LLaMA3-70B (via Groq)
- RAG: ChromaDB + Sentence Transformers

## Estrutura do projeto
```
app.py                # Aplicação principal
rag_chain.py          # Lógica do RAG
chroma_db/            # Banco de dados vetorial
.env                  # Variáveis de ambiente
requirements.txt      # Dependências
```

## Testes

Bibliotecas necessárias:
```
pip install tqdm sentence-transformers scikit-learn
```
Para gerar as respostas:
```
python testAccuracy.py
```
Para avaliar as respostas geradasÇ
```
python calculo_acuracia.py
```

## Documentação relevante
Edital Unicamp 2025: https://www.pg.unicamp.br/norma/31879/0
API Groq: https://console.groq.com/docs
