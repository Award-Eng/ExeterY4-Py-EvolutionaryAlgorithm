import pickle

import funcs


#setting bag number & pop size
POP_SIZE = 100
N_BAGS = 100
T_SIZE = 2 #binary T selection
M_COUNT = 1 #can change but one mutation at start
N_GENERATIONS = 10000 # might be wrong. do check

#reads the file and extracts the data
bags, capacity = funcs.read_file(N_BAGS)



#generates the inital population
pop = funcs.generate_initial_pop(bags, POP_SIZE, capacity)

best_fitnesses = []
best_members = []

for generation in range(N_GENERATIONS):
    parent_a = funcs.tournament_selection(pop, bags, capacity, T_SIZE)
    parent_b = funcs.tournament_selection(pop, bags, capacity, T_SIZE)

    child_c, child_d = funcs.crossover(parent_a, parent_b)
    
    funcs.mutate(child_c, M_COUNT)
    funcs.mutate(child_d, M_COUNT)

    funcs.update_pop(pop, child_c, bags, capacity)
    funcs.update_pop(pop, child_d, bags, capacity)

    best_fitness, best_member = funcs.get_best_fitness(pop, bags, capacity)
    best_fitnesses.append(best_fitness)
    best_members.append(best_member)

    if generation % 100 == 0:
        print(f"Best fitness: {best_fitness}")

# use pickle to save the best_fitnesses list
with open("fitnessGraph.pkl", "wb") as f:
    pickle.dump(best_fitnesses, f)
