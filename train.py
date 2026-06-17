import os
import random
import numpy as np
import pandas as pd

# ==========================================
# CONFIGURAÇÕES
# ==========================================

EPISODES = 5000
STEPS_PER_EPISODE = 30
ALPHA = 0.1
GAMMA = 0.9
EPSILON = 0.1

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

# ==========================================
# CARREGAR DATASET SINTÉTICO
# ==========================================

dataset_path = os.path.join(DATA_DIR, "estudantes_simulados.csv")

df_estudantes = pd.read_csv(dataset_path)

ESTADOS_INICIAIS = list(
    df_estudantes[
        ["motivacao_num", "estresse_num", "desempenho_num", "frequencia_num"]
    ].itertuples(index=False, name=None)
)

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
# ESTADO INICIAL A PARTIR DO DATASET
# ==========================================

def random_state_from_dataset():
    return random.choice(ESTADOS_INICIAIS)

# ==========================================
# TRANSIÇÕES DO AMBIENTE
# ==========================================

def apply_action(state, action):
    motivacao, estresse, desempenho, frequencia = state

    if action == 0:  # estudar sozinho
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

    elif action == 4:  # apoio pedagógico
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
    state = random_state_from_dataset()
    total_reward = 0

    for step in range(STEPS_PER_EPISODE):

        if random.random() < EPSILON:
            action = random.randint(0, len(ACTIONS) - 1)
        else:
            action = int(np.argmax(get_q(state)))

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
# EXPORTAR RECOMPENSAS
# ==========================================

df_rewards = pd.DataFrame({
    "episode": range(len(rewards_history)),
    "reward": rewards_history
})

df_rewards.to_csv(
    os.path.join(DATA_DIR, "recompensas.csv"),
    index=False
)

# ==========================================
# EXPORTAR POLÍTICA APRENDIDA
# ==========================================

policy = []

for state in sorted(q_table.keys()):
    best_action = int(np.argmax(q_table[state]))

    policy.append({
        "estado": str(state),
        "motivacao": state[0],
        "estresse": state[1],
        "desempenho": state[2],
        "frequencia": state[3],
        "acao": ACTIONS[best_action]
    })

pd.DataFrame(policy).to_csv(
    os.path.join(DATA_DIR, "politica.csv"),
    index=False
)

print("\nTreinamento concluído com base no dataset sintético.")
print("Arquivo salvo: data/recompensas.csv")
print("Arquivo salvo: data/politica.csv")
print(f"Registros do dataset: {len(df_estudantes)}")
print(f"Estados iniciais carregados: {len(ESTADOS_INICIAIS)}")
print(f"Estados aprendidos: {len(q_table)}")
print(f"Episódios: {EPISODES}")
print(f"Decisões simuladas: {EPISODES * STEPS_PER_EPISODE}")