# 🎓 PermanecerAI

Sistema Inteligente de Apoio à Permanência Estudantil utilizando Aprendizado por Reforço (Q-Learning).

## 📌 Sobre o Projeto

O PermanecerAI é um projeto acadêmico desenvolvido para demonstrar a aplicação de técnicas de **Aprendizado por Reforço (Reinforcement Learning)** em um problema de relevância social: a permanência estudantil no ensino superior.

O sistema simula diferentes situações enfrentadas por estudantes universitários e treina um agente inteligente para aprender quais ações tendem a produzir melhores resultados em termos de motivação, desempenho acadêmico, frequência e redução do estresse.

O aprendizado é realizado por meio do algoritmo **Q-Learning**, permitindo que o agente aprenda por tentativa e erro, sem a necessidade de dados previamente rotulados.

---

## 🎯 Objetivo

Desenvolver um agente baseado em Aprendizado por Reforço capaz de aprender estratégias que favoreçam a permanência estudantil em um ambiente universitário simulado.

---

## 🧠 Conceitos Utilizados

* Inteligência Artificial
* Aprendizado por Reforço (Reinforcement Learning)
* Q-Learning
* Estados
* Ações
* Recompensas
* Política Aprendida
* Simulação de Ambiente

---

## 🏗️ Modelagem do Problema

### Estado do Estudante

Cada estudante é representado por quatro indicadores:

* Motivação
* Estresse
* Desempenho Acadêmico
* Frequência

Cada variável assume três níveis:

```text
0 = Baixo
1 = Médio
2 = Alto
```

Exemplo:

```text
(0, 2, 1, 0)

Motivação: Baixa
Estresse: Alto
Desempenho: Médio
Frequência: Baixa
```

---

### Ações Possíveis

O agente pode escolher entre as seguintes ações:

* Estudar sozinho
* Descansar
* Participar de monitoria
* Realizar atividade física
* Procurar apoio pedagógico
* Participar de grupo de estudos

---

### Recompensa

A recompensa foi projetada para incentivar:

✅ Maior motivação

✅ Melhor desempenho acadêmico

✅ Maior frequência

✅ Menor estresse

O agente recebe recompensas ou penalidades de acordo com os resultados de suas ações.

---

## ⚙️ Algoritmo Utilizado

O projeto utiliza o algoritmo **Q-Learning**, uma das técnicas mais conhecidas de Aprendizado por Reforço.

Fórmula de atualização:

```text
Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') − Q(s,a)]
```

Onde:

* Q(s,a) = valor da ação no estado atual
* α = taxa de aprendizado
* γ = fator de desconto
* r = recompensa recebida
* s' = próximo estado

---

## 📊 Treinamento

Configuração utilizada:

```text
5000 episódios
30 passos por episódio
150.000 decisões simuladas
```

Durante o treinamento o agente explora o ambiente, recebe recompensas e atualiza sua política de decisão.

---

## 📈 Resultados

Os resultados demonstraram evolução progressiva das recompensas ao longo dos episódios.

A curva de aprendizado apresentou:

* Crescimento consistente da recompensa média;
* Redução do comportamento aleatório;
* Convergência da política aprendida.

Esses resultados indicam que o agente conseguiu aprender estratégias mais eficientes dentro do ambiente simulado.

---

## 🖥️ Dashboard Interativo

O projeto inclui um dashboard desenvolvido em Streamlit que permite:

* Simular diferentes perfis de estudantes;
* Consultar recomendações do agente;
* Visualizar a evolução do treinamento;
* Entender o funcionamento do Aprendizado por Reforço;
* Explorar a política aprendida.

---

## 📂 Estrutura do Projeto

```text
permanecer_ai/
│
├── app.py
├── train.py
├── analise.py
├── README.md
├── requirements.txt
│
└── data/
    ├── recompensas.csv
    └── politica.csv
```

## 🔬 Trabalhos Futuros

* Utilização de dados reais de estudantes;
* Integração com ambientes virtuais de aprendizagem;
* Personalização das recomendações;
* Comparação entre Q-Learning e SARSA;
* Aplicação em programas institucionais de permanência estudantil.

---

## 👨‍💻 Autores

Projeto acadêmico desenvolvido para a disciplina de Aprendizado por Reforço.

**PermanecerAI — Sistema Inteligente de Apoio à Permanência Estudantil**
