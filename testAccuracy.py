import json
from rag_chain import get_answer  # Certifique-se de que essa função está funcionando
from tqdm import tqdm

# Carrega as perguntas e respostas esperadas
with open("data/freq_quest.json", "r", encoding="utf-8") as f:
    perguntas = json.load(f)

# Lista para armazenar os resultados
resultados = []

# Loop pelas perguntas
for item in tqdm(perguntas, desc="Testando perguntas"):
    pergunta = item["pergunta"]
    resposta_esperada = item.get("resposta_esperada", "")
    
    try:
        resposta_gerada = get_answer(pergunta)
    except Exception as e:
        resposta_gerada = f"[ERRO] {e}"
    
    resultados.append({
        "pergunta": pergunta,
        "resposta_esperada": resposta_esperada,
        "resposta_gerada": resposta_gerada
    })

# Salva em JSON
with open("data/resultados_chatbot.json", "w", encoding="utf-8") as f:
    json.dump(resultados, f, indent=2, ensure_ascii=False)

print("✅ Respostas salvas em 'resultados_chatbot.json'")
