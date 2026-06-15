import ast
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="PermanecerAI",
    layout="wide"
)

NIVEIS = {
    "Baixa": 0,
    "Baixo": 0,
    "Média": 1,
    "Médio": 1,
    "Alta": 2,
    "Alto": 2,
}

st.title("🎓 PermanecerAI")
st.subheader("Sistema Inteligente de Apoio à Permanência Estudantil")

st.markdown("""
Este dashboard demonstra um agente treinado com **Aprendizado por Reforço**
usando **Q-Learning** para recomendar ações de apoio à permanência estudantil.
""")

st.divider()

# ==============================
# MÉTRICAS GERAIS
# ==============================

c1, c2, c3, c4 = st.columns(4)

c1.metric("Episódios", "5000")
c2.metric("Decisões simuladas", "150.000")
c3.metric("Estados possíveis", "81")
c4.metric("Ações possíveis", "6")

st.divider()

# ==============================
# COMO O RL FUNCIONA
# ==============================

st.header("Como o Aprendizado por Reforço funciona")

st.graphviz_chart("""
digraph {
    rankdir=LR;

    Estado [label="Estado do estudante\\nMotivação, Estresse, Desempenho, Frequência"]
    Agente [label="Agente\\nQ-Learning"]
    Acao [label="Ação recomendada\\nMonitoria, Descanso, Apoio..."]
    Ambiente [label="Ambiente simulado\\nRotina universitária"]
    Recompensa [label="Recompensa\\nMelhora ou piora do estudante"]

    Estado -> Agente
    Agente -> Acao
    Acao -> Ambiente
    Ambiente -> Recompensa
    Recompensa -> Agente
}
""")

st.info("""
O agente observa o estado atual do estudante, escolhe uma ação, recebe uma recompensa
e atualiza sua política. Com várias tentativas, ele aprende quais ações tendem a
favorecer a permanência estudantil.
""")

st.divider()

# ==============================
# MODELAGEM
# ==============================

st.header("Modelagem do problema")

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.subheader("Estado")
    st.write("""
    O estado representa a situação atual do estudante:

    - Motivação
    - Estresse
    - Desempenho acadêmico
    - Frequência
    """)

with col_b:
    st.subheader("Ações")
    st.write("""
    O agente pode recomendar:

    - Estudar sozinho
    - Descansar
    - Participar de monitoria
    - Fazer atividade física
    - Procurar apoio pedagógico
    - Participar de grupo de estudos
    """)

with col_c:
    st.subheader("Recompensa")
    st.write("""
    A recompensa aumenta quando:

    - melhora o desempenho
    - melhora a frequência
    - aumenta a motivação
    - reduz o estresse
    """)

st.divider()

# ==============================
# SIMULADOR
# ==============================

st.header("Simulador de recomendação")

col1, col2 = st.columns(2)

with col1:
    motivacao = st.selectbox("Motivação", ["Baixa", "Média", "Alta"])
    estresse = st.selectbox("Estresse", ["Baixo", "Médio", "Alto"])

with col2:
    desempenho = st.selectbox("Desempenho", ["Baixo", "Médio", "Alto"])
    frequencia = st.selectbox("Frequência", ["Baixa", "Média", "Alta"])

estado = (
    NIVEIS[motivacao],
    NIVEIS[estresse],
    NIVEIS[desempenho],
    NIVEIS[frequencia],
)

politica = pd.read_csv("data/politica.csv")
politica["estado_tuple"] = politica["estado"].apply(ast.literal_eval)

linha = politica[politica["estado_tuple"] == estado]

st.subheader("Recomendação do agente")

if not linha.empty:
    acao = linha.iloc[0]["acao"]

    st.success(f"Ação recomendada pelo Q-Learning: **{acao}**")

    st.caption(
        f"Estado analisado: motivação={motivacao}, estresse={estresse}, "
        f"desempenho={desempenho}, frequência={frequencia}"
    )
else:
    st.warning("Esse estado não foi encontrado na política aprendida.")

st.divider()

# ==============================
# APRENDIZADO
# ==============================

st.header("Evolução do aprendizado")

df = pd.read_csv("data/recompensas.csv")
df["media_movel"] = df["reward"].rolling(100).mean()

inicio = df.head(500)["reward"].mean()
fim = df.tail(500)["reward"].mean()
ganho = ((fim - inicio) / inicio) * 100

m1, m2, m3 = st.columns(3)

m1.metric("Média inicial", f"{inicio:.2f}")
m2.metric("Média final", f"{fim:.2f}")
m3.metric("Melhoria estimada", f"{ganho:.1f}%")

st.line_chart(
    df.set_index("episode")[["reward", "media_movel"]]
)

st.write("""
A curva de aprendizado mostra a evolução da recompensa ao longo dos episódios.
No início, o agente ainda explora ações quase aleatórias. Com o treinamento,
ele passa a escolher ações que geram recompensas maiores.

Quando a média móvel estabiliza, entendemos que o agente convergiu para uma
política de decisão mais consistente.
""")

st.divider()

# ==============================
# POLÍTICA APRENDIDA
# ==============================

st.header("Política aprendida")

st.write("""
A tabela abaixo mostra exemplos de estados e ações escolhidas pelo agente após o treinamento.
Cada estado é representado por quatro valores:

`(motivação, estresse, desempenho, frequência)`

Onde:

- `0 = baixo`
- `1 = médio`
- `2 = alto`
""")

st.dataframe(
    politica[["estado", "acao"]],
    use_container_width=True
)

st.divider()

# ==============================
# LIMITAÇÕES
# ==============================

st.header("Limitações e trabalhos futuros")

st.warning("""
Este projeto é uma simulação acadêmica. Ele não substitui professores, pedagogos,
psicólogos ou políticas institucionais de permanência estudantil.
""")

st.write("""
Como evolução, o modelo poderia ser treinado com dados reais de estudantes,
histórico de frequência, desempenho acadêmico, participação em monitorias e indicadores
de risco de evasão.
""")