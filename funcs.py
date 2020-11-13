"""
This module contains the functions used to run mainCode.py
"""

import random


class Bag:
    """
    Class which stores the bag number, weight and value
    """
    def __init__(self, id, weight, value):
        self.id = id
        self.weight = weight
        self.value = value

    #makes the data more user friendly to read
    def __repr__(self):
        return f"{{id: {self.id}, weight: {self.weight}, value: {self.value}}}"


def read_file(n_bags):
    """
    This function reads the data from the file BankProblem.txt and extracts the capacity of the van
    and the weight, value and number of each of the 100 bags before storing that data in the class Bag
    """
    bags = []

    with open("BankProblem.txt") as fobj:  

        #reads the end of the line to obtain the vans capacity
        capacity = float(fobj.readline().split()[-1])

        #reads the bag number, weight and value
        for i in range(n_bags):
            bag_line = fobj.readline()
            weight_line = fobj.readline()
            value_line = fobj.readline()

            #removes the whitespace and ':' from bag line and extract number    
            id = int(bag_line.strip().strip(":").split()[1])
            weight = float(weight_line.split()[1])
            value = float(value_line.split()[1])

            #adds each bag to a list of bags in the Class Bag
            bag = Bag(id, weight, value)
            bags.append(bag)
    
    return bags, capacity


def generate_initial_pop(bags,pop_size, max_weight):
    """
    This function generates an initial population of pop_size randomly generated solutions from the class Bags 
    and then outputs a binary list saying if a bag is present or not. It returns a list of pop_members each
    containing a list of bags
    """
    pop = []
    for i in range(pop_size):
        pop_member = []

        #uses binary to represent if a bag is in the population or not
        for j in range(len(bags)):
            pop_member.append(random.randint(0, 1))

        pop.append(pop_member)

    return pop


def evaluate_fitness(pop_member, bags, max_weight):
    """
    This function evaluates the fitness of each population member by calculating the monetary value of each
    up to the weight capacity defined by the BankProblem.txt file
    """
    total_weight = 0
    total_value = 0

    #pairs the first item of pop_member and bags together and repeats for each subsequent member
    #allowing the evalulation of the fitness for the population. If the bag is present in the population
    #then the weight and value of it will be read. If the bag is not, it moves onto the next one
    for flag, bag in zip(pop_member, bags):
        if flag == 1:
            total_weight += bag.weight
            total_value += bag.value

    #returns the fitness if the weight is under the capacity of the van else returns 0
    if total_weight <= max_weight:
        return total_value
    else:
        return 0


def tournament_selection(pop, bags, max_weight, t_size):
    """
    This function uses Tournament Selection to optain a single parent by randomly picking t_size
    number of parents from the population and then selecting the parent with the best fitness. 
    Or in case of a draw, randomly selecting between the two
    """
    #randomly chooses t_size number of chromosomes from the list
    parents = random.choices(pop, k=t_size)

    #evalulates the fitness of the chromosome in the list
    fittest_parent = parents[0]
    current_best_fitness = evaluate_fitness(fittest_parent, bags, max_weight)
    
    #checks each other chromosome in the list to see if their fitness is great. If so they become the dominant chromosome
    #if a tie occurs, one of them is randomly selected
    for parent_member in parents[1:]:
        new_fitness = evaluate_fitness(parent_member, bags, max_weight)
        
        if new_fitness > current_best_fitness:
            current_best_fitness = new_fitness
            fittest_parent = parent_member
        elif new_fitness == current_best_fitness:
            if random.random() < 0.5:
                current_best_fitness = new_fitness
                fittest_parent = parent_member

    return fittest_parent


def crossover(parent_a, parent_b):
    """
    This function performs a single point crossover on the parents to return two children
    """
    #picks a random split point
    split_point = random.randint(0, len(parent_a)-1)

    #combines both parents at the random split point to give two children
    child_c = parent_a[:split_point] + parent_b[split_point:]
    child_d = parent_b[:split_point] + parent_a[split_point:]

    return child_c, child_d


def mutate(child, m_count):
    """
    Performs a random mutation on both children
    """
    #selects the random point for the mutation and flips the binary bit round. Either adding (1) or
    #removing (0) a bag from the childs index
    for i in range(m_count):
        idx = random.randint(0, len(child)-1)

        if child[idx] == 1:
            child[idx] = 0
        else:
            child[idx] = 1


def update_pop(pop, child, bags, max_weight):
    """
    This function evaluates the fitness of each member of the population and finds the lowest value.
    Before replacing it with the mutated values of the child should the childs fitness be greater than it. 
    If it is equal then it randomly selects one. This function performs Weakest Replacement
    """
    worst_member = pop[0]
    #sets the first value in the population list to be the minimum fitness
    min_fitness = evaluate_fitness(worst_member, bags, max_weight)

    #finds the worest fitness in the current population updating as it finds a lower value
    for pop_member in pop[1:]:
        fitness = evaluate_fitness(pop_member, bags, max_weight)

        if fitness < min_fitness:
            min_fitness = fitness
            worst_member = pop_member

    #determine the fitness of the mutated child
    child_fitness = evaluate_fitness(child, bags, max_weight)

    #replaces the weakest population member with the mutated child if the childs fitness is
    #greater then the weakest population member
    if child_fitness > min_fitness:
        pop.remove(worst_member)
        pop.append(child)
    elif child_fitness == min_fitness:
        if random.random() < 0.5:
            pop.remove(worst_member)
            pop.append(child)


def get_best_fitness(pop, bags, max_weight):
    """
    This function determines the best fitness of each generation
    """
    best_member = pop[0]
    max_fitness = evaluate_fitness(best_member, bags, max_weight)

    #finds the best fitness in the current population updating as it finds a higher value
    for pop_member in pop[1:]:
        fitness = evaluate_fitness(pop_member, bags, max_weight)

        if fitness > max_fitness:
            max_fitness = fitness
            best_member = pop_member
    return max_fitness, best_member