import pickle

import matplotlib.pyplot as plt


with open("fitnessGraph.pkl", "rb") as f:
    best_fitnesses = pickle.load(f)

plt.plot(best_fitnesses)

plt.xlabel("Generation")
plt.ylabel("Fitness")

plt.savefig("figure.png")