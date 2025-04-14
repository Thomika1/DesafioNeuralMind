import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Carrega as respostas salvas do seu chatbot
with open("data/resultados_chatbot.json", "r", encoding="utf-8") as f:
    resultados = json.load(f)

# Modelo para embeddings (pode trocar por um mais pesado se quiser mais precisão)
model = SentenceTransformer("all-MiniLM-L6-v2")

similaridades = []

for item in resultados:
    esperada = item["resposta_esperada"]
    gerada = item["resposta_gerada"]

    # Cria embeddings
    embeddings = model.encode([esperada, gerada])
    
    # Similaridade cosseno
    sim = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    item["similaridade"] = float(sim)
    similaridades.append(sim)

# Estatísticas
media = np.mean(similaridades)
desvio = np.std(similaridades)
acima_de_0_75 = sum(1 for s in similaridades if s >= 0.75) / len(similaridades)

# Print resumo
print(f"\n📊 Avaliação das respostas:")
print(f"🔹 Similaridade média: {media:.4f}")
print(f"🔹 Desvio padrão: {desvio:.4f}")
print(f"🔹 Porcentagem com similaridade ≥ 0.75: {acima_de_0_75 * 100:.2f}%")

# Salva os resultados com similaridade
with open("data/avaliacao_chatbot.json", "w", encoding="utf-8") as f:
    json.dump(resultados, f, indent=2, ensure_ascii=False)
