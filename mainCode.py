import funcs

#setting bag number & pop size
POP_SIZE = 10
N_BAGS = 10
T_SIZE = 2 #binary T selection
M_COUNT = 1 #can change but one mutation at start
N_GENERATIONS = 10000 # might be wrong. do check

#reads the file and extracts the data
bags, capacity = funcs.read_file(N_BAGS)



#generates the inital population
pop = funcs.generate_initial_pop(bags, POP_SIZE, capacity)

best_fitnesses = []

for generation in range(N_GENERATIONS):
    #evaluates the fitness of the entire population - highest 3000 odd, lowest 2K 
    #for pop_member in pop:
        #print(pop_member.fitness)

    #rank fitnesss

    #t_selection
    parent_a = funcs.tournament_selection(pop, bags, capacity, T_SIZE)
    parent_b = funcs.tournament_selection(pop, bags, capacity, T_SIZE)

    child_c, child_d = funcs.crossover(parent_a, parent_b)
    
    funcs.mutate(child_c, M_COUNT)
    funcs.mutate(child_d, M_COUNT)

    funcs.update_pop(pop, child_c, bags, capacity)
    funcs.update_pop(pop, child_d, bags, capacity)

    best_fitness = funcs.get_best_fitness(pop)
    best_fitnesses.append(best_fitness)

# use pickle to save the best_fitnesses list
