import random

#class holding the bag number, weight and value of it for all bags
class Bag:

    def __init__(self, id, weight, value):
        self.id = id
        self.weight = weight
        self.value = value


    def __repr__(self):
        return f"{{id: {self.id}, weight: {self.weight}, value: {self.value}}}"


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
                       
            id = int(bag_line.strip().strip(":").split()[1])
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
        pop_member = []
        for j in range(len(bags)):
            pop_member.append(random.randint(0, 1))

        pop.append(pop_member)

    return pop #list of pop_members containing a list of bags

def evaluate_fitness(pop_member, bags, max_weight):
    """
    This function evaluates the fitness of each population member by calculating the monetary value of each
    up to the capacity defined by the BankProblem.txt file. After that each subsequent bag is ignored
    """
    total_weight = 0
    total_value = 0
    for flag, bag in zip(pop_member, bags):
        if flag == 1:
            total_weight += bag.weight
            total_value += bag.value

    if total_weight <= max_weight:
        return total_value
    else:
        return 0


def tournament_selection(pop, bags, max_weight, t_size):
    """
    This function uses Binary Tournament Selection to optain a single parent by randomly picking two,
    then selecting the parent with the better fitness. Or in case of a draw randomly selecting the parent
    """
    
    parents = random.choices(pop, k=t_size) #t_size gets 2 random elements from list

    parent1 = parents[0]
    parent2 = parents[1]

    fitness1 = evaluate_fitness(parent1, bags, max_weight)
    fitness2 = evaluate_fitness(parent2, bags, max_weight)

    #call the fitness
    if fitness1 > fitness2:
        return parent1
    elif fitness1 == fitness2:
        return random.choice(parents)
    else:
        return parent2


def update_pop(pop, child, bags, max_weight):
    """
    This function evaluates the fitness of each member of the population and finds the lowest value.
    Before then swapping it with the mutated values of each child should it be lower then they are. If
    equal then it randomly selects one
    """
    worst_member = pop[0]
    min_fitness = evaluate_fitness(worst_member, bags, max_weight)

    for pop_member in pop[1:]:
        fitness = evaluate_fitness(pop_member, bags, max_weight)

        if fitness < min_fitness:
            min_fitness = fitness
            worst_member = pop_member

    child_fitness = evaluate_fitness(child, bags, max_weight)
    if child_fitness > min_fitness:
        pop.remove(worst_member)
        pop.append(child)
    elif child_fitness == min_fitness:
        if random.random() < 0.5:
            pop.remove(worst_member)
            pop.append(child)


#crossover of parents
def crossover(parent_a, parent_b):
    split_point = random.randint(0, len(parent_a)-1)

    child_c = parent_a[:split_point] + parent_b[split_point:]
    child_d = parent_b[:split_point] + parent_a[split_point:]
    #combine both parents to give 2 children

    return child_c, child_d


#mutations of children and eval fitness
def mutate(child, m_count):
    for i in range(m_count):
        idx = random.randint(0, len(child)-1)

        if child[idx] == 1:
            child[idx] = 0
        else:
            child[idx] = 1


def get_best_fitness(pop, bags, max_weight):
    best_member = pop[0]
    max_fitness = evaluate_fitness(best_member, bags, max_weight)

    for pop_member in pop[1:]:
        fitness = evaluate_fitness(pop_member, bags, max_weight)

        if fitness > max_fitness:
            max_fitness = fitness
            best_member = pop_member
    return max_fitness, best_member