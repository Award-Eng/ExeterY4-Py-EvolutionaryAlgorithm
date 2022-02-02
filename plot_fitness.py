"""
This module plots the best fitness of each generation in a graph before displaying it as
the figure bestFitnesses.png
"""
"""
Imports modules needed for plotting the results
"""
import pickle

import matplotlib.pyplot as plt

#loads the best fitness values of each generation from the file
with open("fitnessGraphData.pkl", "rb") as f:
    best_fitnesses = pickle.load(f)

#plots a graph of the best fitnesses
plt.plot(best_fitnesses)
plt.xlabel("Generation")
plt.ylabel("Fitness")

#saves the figure
plt.savefig("bestFitnesses.png")