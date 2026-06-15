import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/recompensas.csv")

df["media_movel"] = df["reward"].rolling(100).mean()

plt.figure(figsize=(12,6))

plt.plot(df["episode"], df["reward"],
         alpha=0.3,
         label="Recompensa")

plt.plot(df["episode"],
         df["media_movel"],
         linewidth=3,
         label="Média móvel (100 episódios)")

plt.title("Aprendizado do Agente")
plt.xlabel("Episódios")
plt.ylabel("Recompensa")

plt.legend()
plt.grid()

plt.show()