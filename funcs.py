import random
import pickle

#class holding the bag number, weight and value of it for all bags
class Bag:

    def __init__(self, id, weight, value):
        self.id = id
        self.weight = weight
        self.value = value


    def __repr__(self):
        return f"{{id: {self.id}, weight: {self.weight}, value: {self.value}}}"


class PopulationMember:

    def __init__(self, bags, max_weight):
        self.bags = bags
        self.fitness = evaluate_fitness(bags, max_weight)


def read_file(n_bags):
"""
    This function reads the input from the file BankProblem.txt and extracts the capacity of the van
    and the weight, value and number of each of the 100 bags before storing that data in the class Bag
"""
    bags = []

    with open("BankProblem.txt") as fobj:      
    #data = fobj.read()
    #print(data)

        capacity = float(fobj.readline().split()[-1])
    #while True:
        for i in range(n_bags):
            bag_line = fobj.readline()
            weight_line = fobj.readline()
            value_line = fobj.readline()
                       
            id = int(bag_line.strip(": ").split()[1])
            weight = float(weight_line.split()[1])
            value = float(value_line.split()[1])

            bag = Bag(id, weight, value)
            bags.append(bag)
    
    return bags, capacity

def generate_initial_pop(bags,pop_size, max_weight):
"""
    This function generates an initial population of pop_size randomly generated solutions from the class Bags and
    stores the results in another Class PopulationMember before returning a list of pop_members containing a list of
    bags
"""
    pop = []
    for i in range(pop_size):
        soln = bags.copy()
        random.shuffle(soln)
        pop_member = PopulationMember(soln, max_weight)
        pop.append(pop_member)
    return pop #list of pop_members containing a list of bags

def evaluate_fitness(bags, max_weight):
    """
    This function evaluates the fitness of each population member by calculating the monetary value of each
    up to the capacity defined by the BankProblem.txt file. After that each subsequent bag is ignored
    """
    fitness = 0
    total_weight = 0
    for bag in bags:
        total_weight += bag.weight

        if total_weight > max_weight:
            return fitness
        
        fitness += bag.value
    return fitness


def tournament_selection(t_size, pop):
    """
    This function uses Binary Tournament Selection to optain a single parent by randomly picking two,
    then selecting the parent with the better fitness. Or in case of a draw randomly selecting the parent
    """
    
    parents = random.choices(pop, k=t_size) #t_size gets 2 random elements from list

    parent1 = parents[0]
    parent2 = parents[1]

    #call the fitness
    if parent1.fitness > parent2.fitness:
        return parent1
    elif parent1.fitness == parent2.fitness:
        random.choice(parents)
    else:
        return parent2


def update_pop(pop, mutation):
"""
    This function evaluates the fitness of each member of the population and finds the lowest value.
    Before then swapping it with the mutated values of each child should it be lower then they are. If
    equal then it randomly selects one
"""
    worst_member = pop[0]
    min_fitness = worst_member.fitness

    for pop_member in pop[1:]:
        if pop_member.fitness < min_fitness:
            min_fitness = pop_member.fitness
            worst_member = pop_member

    if mutation.fitness > min_fitness:
        pop.remove(worst_member)
        pop.append(mutation)
        #If equal

"""

#crossover of parents
def crossover(parent_a, parent_b):
    split_point = random.random()*len(parent_a)
    #combine both parents to give 2 children


#mutations of children and eval fitness
def mutation(child_c, child_d, m_rate, bags):
    for i to range(m_rate)

    #evalulate fitness again
    return mutation_e, mutation_f
#replace weakest
def replace_weakest(mutation_e, mutation_f):
    if mutation_e.Fitness > bags.Fitness:
        pass
        #overwrite bag value
    else:
        pass
    #nothing

    if mutation.f.Fitness > bags.Fitness:
        pass
    #repeat of other one 

#back to binary tournament unless reaching 10,000 fitness evaluations
#how to record the best fitness at the end of each trial & show results??
"""

def store_best_fitness(best_fitnesses):
    graph_file = open("fitnessGraph.pkl", "w")
    pickle.dump(best_fitnesses, graph_file)
    graph_file.close()