import pickle

import matplotlib.pyplot as plt


# Load the pickle list
#best_fitnesses = pickle.load(...)
best_fitnesses = range(100)

graph_file_open = open("fitnessGraph.pkl", "r")
best_fitnesses = pickle.load(graph_file_open)
graph_file_open.close()

plt.plot(best_fitnesses)

plt.xlabel("Generation")
plt.ylabel("Fitness")

plt.show()
plt.savefig("figure.png")