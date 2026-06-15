import random
import numpy as np
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)
# ==========================================
# CONFIGURAÇÕES
# ==========================================

EPISODES = 5000
ALPHA = 0.1
GAMMA = 0.9
EPSILON = 0.1

# ==========================================
# AÇÕES
# ==========================================

ACTIONS = {
    0: "Estudar Sozinho",
    1: "Descansar",
    2: "Participar de Monitoria",
    3: "Atividade Física",
    4: "Apoio Pedagógico",
    5: "Grupo de Estudos"
}

# ==========================================
# ESTADOS
# Cada variável:
# 0 = baixo
# 1 = médio
# 2 = alto
# ==========================================

def random_state():
    return (
        random.randint(0, 2),  # motivação
        random.randint(0, 2),  # estresse
        random.randint(0, 2),  # desempenho
        random.randint(0, 2),  # frequência
    )

# ==========================================
# TRANSIÇÕES DO AMBIENTE
# ==========================================

def apply_action(state, action):

    motivacao, estresse, desempenho, frequencia = state

    if action == 0:  # estudar
        desempenho = min(2, desempenho + 1)
        estresse = min(2, estresse + 1)

    elif action == 1:  # descansar
        estresse = max(0, estresse - 1)
        motivacao = min(2, motivacao + 1)

    elif action == 2:  # monitoria
        desempenho = min(2, desempenho + 1)
        frequencia = min(2, frequencia + 1)

    elif action == 3:  # atividade física
        estresse = max(0, estresse - 1)
        motivacao = min(2, motivacao + 1)

    elif action == 4:  # apoio
        motivacao = min(2, motivacao + 1)
        estresse = max(0, estresse - 1)

    elif action == 5:  # grupo de estudos
        desempenho = min(2, desempenho + 1)
        motivacao = min(2, motivacao + 1)

    next_state = (
        motivacao,
        estresse,
        desempenho,
        frequencia
    )

    reward = (
        motivacao * 2
        + desempenho * 3
        + frequencia * 3
        - estresse * 2
    )

    return next_state, reward

# ==========================================
# Q-TABLE
# ==========================================

q_table = {}

def get_q(state):

    if state not in q_table:
        q_table[state] = np.zeros(len(ACTIONS))

    return q_table[state]

# ==========================================
# TREINAMENTO
# ==========================================

rewards_history = []

for episode in range(EPISODES):

    state = random_state()
    total_reward = 0

    for step in range(30):

        if random.random() < EPSILON:
            action = random.randint(0, 5)
        else:
            action = np.argmax(get_q(state))

        next_state, reward = apply_action(state, action)

        old_q = get_q(state)[action]

        next_max = np.max(get_q(next_state))

        new_q = old_q + ALPHA * (
            reward + GAMMA * next_max - old_q
        )

        get_q(state)[action] = new_q

        state = next_state
        total_reward += reward

    rewards_history.append(total_reward)

# ==========================================
# EXPORTAR RESULTADOS
# ==========================================

df_rewards = pd.DataFrame({
    "episode": range(len(rewards_history)),
    "reward": rewards_history
})

df_rewards.to_csv(
    os.path.join(DATA_DIR, "recompensas.csv"),
    index=False
)

policy = []

for state in q_table:

    best_action = np.argmax(q_table[state])

    policy.append({
        "estado": str(state),
        "acao": ACTIONS[best_action]
    })

pd.DataFrame(policy).to_csv(
    os.path.join(DATA_DIR, "politica.csv"),
    index=False
)

print("\nTreinamento concluído.")
print("Arquivo salvo: data/recompensas.csv")
print("Arquivo salvo: data/politica.csv")
print(f"Estados aprendidos: {len(q_table)}")




