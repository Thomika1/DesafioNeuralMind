# Chatbot Vestibular Unicamp 2025

A versão hospedada na nuvem do chat bot pode ser encontrada em: [Link](https://desafionm.streamlit.app/)

Assistente virtual para tirar dúvidas sobre o vestibular da Unicamp 2025, baseado na Resolução GR-029/2024.

## Pré-requisitos

- Python 3.10 ou superior
- Poetry (ou pip)
- Conta na Groq (para API key)

## Como executar localmente

Importante: comente as linha ```__import__('pysqlite3')``` e ```sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')```
do arquivo rag_chain.py para rodar localmente. Essas linhas são usadas para que o chatbot rode no cloud da streamlit, porém acarretam em erros ao rodar localmente.

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
.
├── chroma_db/                            # Banco vetorial (ChromaDB) com os embeddings persistidos
├── data/                                 # Arquivos utilizados e gerados na avaliação
│   ├── Procuradoria Geral - Normas.pdf   # Documento base (normas da Unicamp)
│   ├── freq_quest.json                   # Perguntas frequentes usadas para avaliação
│   ├── avaliacao_chatbot.json            # JSON contendo perguntas e respostas esperadas
│   ├── resultados_chatbot.json           # Resultados gerados após testes de acurácia
├── .env                                  # Variáveis de ambiente (API keys, configs)
├── .gitignore                            # Arquivos e pastas ignorados pelo Git
├── indexador.py                          # Script que carrega, divide e indexa o PDF no ChromaDB
├── main.py                               # Interface principal do chatbot (ex: Streamlit app)
├── rag_chain.py                          # Lógica do RAG (Retrieval-Augmented Generation)
├── testAccuracy.py                       # Executa testes automáticos com perguntas e salva os resultados
├── calculo_acuracia.py                   # Faz a análise de similaridade e acurácia
├── text.py                               # Script para melhorar a estrutura do documento que irá alimentar o modelo
├── requirements.txt                      # Lista de dependências do projeto
└── README.md                             # Este arquivo de documentação

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
Para avaliar as respostas geradas:
```
python calculo_acuracia.py
```

## Conclusões testes
De acordo com os testes realizados, a similaridade média obtida foi de 0.5514, considerando que essa métrica varia de 0 a 1.0, sendo que valores mais altos indicam maior proximidade semântica entre a resposta gerada pelo modelo e a resposta esperada.

Observou-se um desvio significativo na média devido a perguntas específicas. Por exemplo, a pergunta "A Unicamp oferece alojamento para os candidatos no dia da prova?" obteve uma similaridade de apenas 0.14, mesmo com uma resposta correta, o que evidencia limitações na avaliação puramente semântica.

Esse tipo de discrepância contribuiu para a redução da média geral de similaridade, indicando que, apesar de o modelo fornecer respostas adequadas em diversos casos, a métrica de similaridade semântica nem sempre reflete corretamente a qualidade da resposta.

## Documentação relevante
Edital Unicamp 2025: https://www.pg.unicamp.br/norma/31879/0
API Groq: https://console.groq.com/docs
