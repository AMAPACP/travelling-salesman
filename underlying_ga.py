from deap import creator
from deap import tools
from deap import base
import numpy as np
import destinations as dest


# Some general notes on type creation
# Basically, using the creator.create function, you make a class with a name, data type, some attributes
# The toolbox.register function allows you to initialize instances of these containers

def create_containers(size):
    creator.create("FitMin", base.Fitness, value=(-0.1,))
    creator.create("Individual", np.ndarray, fitness="FitMin")
    toolbox = base.Toolbox()
    toolbox.register("individual", tools.initRepeat, creator.Individual, np.random.randint(0, 1000000), size)


def evaluate(points, lines):
    order = np.argsort(lines)
    distance = 0
    for i in range(len(lines)):
        distance += dest.calc_distance(points[order[i-1]], points[order[i]])
    lines.fitness = distance
    return lines


def create_first_gen(size, init_method):
    individuals = []
    for i in range(size):
        individuals.append(init_method)
    return individuals


def mutate(individual):
    return tools.mutShuffleIndexes(individual, 1/(len(individual) * 2))


def cross_individuals(ind1, ind2):
    return tools.cxTwoPoint(ind1, ind2)


def make_gen(pre_gen, x_chance):
    selected = tools.selBest(pre_gen, len(pre_gen) / 2)
    clones = [selected[i % len(selected)] for i in range(len(selected))]
    for i in range(len(clones)):
        mutate(clones[i])
        if np.random.random() < x_chance:
            cross_individuals(clones[i-1], clones[i])
    return clones
