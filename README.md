# 🎓 PermanecerAI

Sistema Inteligente de Apoio à Permanência Estudantil utilizando Aprendizado por Reforço (Q-Learning).

## 📌 Sobre o Projeto

O PermanecerAI é um projeto acadêmico desenvolvido para demonstrar a aplicação de técnicas de **Aprendizado por Reforço (Reinforcement Learning)** em um problema de relevância social: a permanência estudantil no ensino superior.

O sistema simula diferentes cenários enfrentados por estudantes universitários e treina um agente inteligente para aprender quais ações tendem a produzir melhores resultados em termos de motivação, desempenho acadêmico, frequência e redução do estresse.

O aprendizado é realizado por meio do algoritmo **Q-Learning**, permitindo que o agente aprenda por tentativa e erro, sem a necessidade de respostas previamente rotuladas.

Além do treinamento do agente, o projeto disponibiliza um dashboard interativo desenvolvido em Streamlit para visualização dos resultados e demonstração da política aprendida.

---

## 🎯 Objetivo

Desenvolver um agente baseado em Aprendizado por Reforço capaz de aprender estratégias que favoreçam a permanência estudantil em um ambiente universitário simulado.

---

## 🧠 Problema Proposto

A evasão universitária é um desafio enfrentado por instituições de ensino em todo o mundo.

Diversos fatores podem influenciar a permanência de um estudante, tais como:

* Baixa motivação;
* Elevado nível de estresse;
* Baixo desempenho acadêmico;
* Baixa frequência às aulas.

O PermanecerAI busca simular esse contexto e identificar quais intervenções tendem a gerar melhores resultados para o estudante.

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
(0,2,1,0)

Motivação = Baixa
Estresse = Alto
Desempenho = Médio
Frequência = Baixa
```

Total de estados possíveis:

```text
3⁴ = 81 estados
```

---

### Ações Possíveis

O agente pode escolher entre:

* Estudar sozinho;
* Descansar;
* Participar de monitoria;
* Fazer atividade física;
* Procurar apoio pedagógico;
* Participar de grupo de estudos.

Total:

```text
6 ações possíveis
```

---

### Recompensa

A função de recompensa foi projetada para incentivar:

✅ aumento da motivação

✅ aumento do desempenho acadêmico

✅ aumento da frequência

✅ redução do estresse

O agente recebe recompensas ou penalidades de acordo com os resultados produzidos por suas ações.

---

## 🔬 Dataset Sintético

Para documentar e validar os cenários do ambiente foi criado um dataset sintético contendo:

```text
243 registros simulados
81 estados possíveis
3 repetições por estado
```

Variáveis:

* Motivação
* Estresse
* Desempenho
* Frequência
* Pontuação de risco
* Risco de evasão

Importante:

> O dataset não foi utilizado para treinar o agente de forma supervisionada. O treinamento ocorreu por interação com o ambiente, conforme a lógica do Aprendizado por Reforço.

Arquivo:

```text
data/estudantes_simulados.csv
```

---

## ⚙️ Algoritmo Utilizado

O projeto utiliza o algoritmo **Q-Learning**, uma das técnicas mais conhecidas de Aprendizado por Reforço.

Fórmula de atualização:

```text
Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') − Q(s,a)]
```

Onde:

* Q(s,a) = qualidade da ação no estado atual;
* α = taxa de aprendizado;
* γ = fator de desconto;
* r = recompensa recebida;
* s' = próximo estado.

---

## 📊 Treinamento

Configuração utilizada:

```text
5000 episódios
30 passos por episódio
150.000 decisões simuladas
```

Durante o treinamento, o agente:

1. Observa o estado do estudante;
2. Escolhe uma ação;
3. Recebe uma recompensa;
4. Atualiza sua Q-Table;
5. Aprende uma política de decisão.

---

## 📈 Resultados Obtidos

Os resultados demonstraram evolução progressiva das recompensas ao longo dos episódios.

Observou-se:

* Crescimento consistente da recompensa média;
* Redução do comportamento aleatório;
* Convergência da política aprendida;
* Estabilização do aprendizado após aproximadamente 1000 episódios.

Esses resultados indicam que o agente conseguiu aprender estratégias mais eficientes dentro do ambiente simulado.

---

## 🖥️ Dashboard Interativo

O projeto inclui um dashboard desenvolvido em Streamlit que permite:

* Visualizar o ciclo do Aprendizado por Reforço;
* Simular diferentes perfis de estudantes;
* Consultar recomendações do agente;
* Visualizar a curva de aprendizado;
* Explorar o dataset sintético;
* Consultar a política aprendida.

---

## 📂 Estrutura do Projeto

```text
permanecer_ai/
│
├── app.py
├── train.py
├── analise.py
├── gerar_dataset.py
├── README.md
├── requirements.txt
│
└── data/
    ├── recompensas.csv
    ├── politica.csv
    └── estudantes_simulados.csv
```

## 🎓 Conceitos Demonstrados

* Aprendizado por Reforço
* Q-Learning
* Ambiente Simulado
* Estado
* Ação
* Recompensa
* Política Aprendida
* Convergência
* Tomada de decisão baseada em IA

---

## 🔮 Trabalhos Futuros

* Utilização de dados reais de estudantes;
* Integração com ambientes virtuais de aprendizagem;
* Comparação entre Q-Learning e SARSA;
* Personalização das recomendações;
* Modelagem mais complexa da evasão estudantil;
* Aplicação em programas institucionais de permanência.

---

## 👨‍💻 Autores

Projeto acadêmico desenvolvido para a disciplina de Aprendizado por Reforço.

**PermanecerAI – Sistema Inteligente de Apoio à Permanência Estudantil**

