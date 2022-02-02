"""
This code runs an evolutionary algorithm (EA) designed to find the largest
sum of money that can be stored in a security van within the constraints
of the total weight supported by the van
"""

"""
Imports the required modules for the code to run
"""
import pickle

import funcs


"""
These are a set of global variables called throughout the program. By being
global, these can then be changed to allow different experiments to be performed 
to test the optimization of the EA
"""
POP_SIZE = 100         #population size
N_BAGS = 100           #number of bags
T_SIZE = 2             #setting the tournament size
M_COUNT = 1            #mutation rate
N_GENERATIONS = 10000  #max number of fitness evalulations


#reads the file and extracts the data from it
bags, capacity = funcs.read_file(N_BAGS)

#generates the inital population
pop = funcs.generate_initial_pop(bags, POP_SIZE, capacity)

best_fitnesses = []
best_members = []

"""
The EA is introduced here and loops round until the termination criteria has
been met
"""
for generation in range(N_GENERATIONS):

    #both parents are determined here
    parent_a = funcs.tournament_selection(pop, bags, capacity, T_SIZE)
    parent_b = funcs.tournament_selection(pop, bags, capacity, T_SIZE)
    
    #creation of the children
    child_c, child_d = funcs.crossover(parent_a, parent_b)
    
    #mutation of each child
    funcs.mutate(child_c, M_COUNT)
    funcs.mutate(child_d, M_COUNT)

    #updates the population with the mutated children if their fitness is 
    #greater then the lowest fitness in the population
    funcs.update_pop(pop, child_c, bags, capacity)
    funcs.update_pop(pop, child_d, bags, capacity)

    #retrieves the highest fitness value of the current generation
    best_fitness, best_member = funcs.get_best_fitness(pop, bags, capacity)
    best_fitnesses.append(best_fitness)
    best_members.append(best_member)

    #prints the current best fitness every 100 values
    if generation % 100 == 0:
        print(f"Best fitness: {best_fitness}")

"""
Stores the best fitness of each generation in a pkl file for plotting in the 
plot_fitness module
"""
with open("fitnessGraphData.pkl", "wb") as f:
    pickle.dump(best_fitnesses, f)
