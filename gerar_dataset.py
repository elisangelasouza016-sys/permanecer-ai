import itertools
import pandas as pd

NIVEIS = {
    0: "Baixa",
    1: "Média",
    2: "Alta"
}

NIVEIS_ESTRESSE = {
    0: "Baixo",
    1: "Médio",
    2: "Alto"
}

registros = []
id_registro = 1

combinacoes = list(itertools.product([0, 1, 2], repeat=4))

for repeticao in range(3):
    for motivacao, estresse, desempenho, frequencia in combinacoes:

        pontuacao_risco = 0

        if motivacao == 0:
            pontuacao_risco += 2
        elif motivacao == 1:
            pontuacao_risco += 1

        if estresse == 2:
            pontuacao_risco += 2
        elif estresse == 1:
            pontuacao_risco += 1

        if desempenho == 0:
            pontuacao_risco += 2
        elif desempenho == 1:
            pontuacao_risco += 1

        if frequencia == 0:
            pontuacao_risco += 2
        elif frequencia == 1:
            pontuacao_risco += 1

        if pontuacao_risco >= 6:
            risco = "Alto"
        elif pontuacao_risco >= 3:
            risco = "Médio"
        else:
            risco = "Baixo"

        registros.append({
            "id": id_registro,
            "motivacao_num": motivacao,
            "estresse_num": estresse,
            "desempenho_num": desempenho,
            "frequencia_num": frequencia,
            "motivacao": NIVEIS[motivacao],
            "estresse": NIVEIS_ESTRESSE[estresse],
            "desempenho": NIVEIS[desempenho],
            "frequencia": NIVEIS[frequencia],
            "pontuacao_risco": pontuacao_risco,
            "risco_evasao": risco
        })

        id_registro += 1

df = pd.DataFrame(registros)

df.to_csv("data/estudantes_simulados.csv", index=False, encoding="utf-8-sig")

print("Dataset sintético criado com sucesso.")
print("Arquivo: data/estudantes_simulados.csv")
print(f"Total de registros: {len(df)}")
print(df.head())