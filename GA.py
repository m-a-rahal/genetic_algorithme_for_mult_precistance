import random
from datetime import datetime
random.seed(datetime.now())
from mult_precistance import Population, Solution, percistance


class GA():
    def __init__(self, N = 100, mutation_rate = 0.4, cross_rate = 0.98, max_iter = 100):
        super().__init__()
        self.N = N
        self.mutation_rate = mutation_rate
        self.cross_rate = cross_rate
        self.max_iter = max_iter
        # indexes used for random mutation spots
        self.indexes = list(range(self.N))

    def solve(self, length = 20):
        population = Population(self.N, length)
        for i in range(self.max_iter):
            children = []
            population.sort(key= lambda x : random.random())
            parents = [(population[2*j], population[2*j+1]) for j in range(len(population)//2)]
            for pair in parents:
                child1 = self.cross(pair[0], pair[1])
                child2 = self.cross(pair[1], pair[0])
                children.append(self.mutate(child1))
                children.append(self.mutate(child2))
            for child in children:
                population.add(child)
            population.reduce_to_size() # this also sorts the population

        return population[0] # return best 

    def cross(self, sol1, sol2):
        if (random.random() < self.cross_rate):
            return Solution([sol1[i] if random.random() > 0.5 else sol2[i] for i in range(len(sol1))])
        else:
            return sol1

    def mutate(self, sol):
        if (random.random() < self.mutation_rate):
            return sol.mutate(self.mutation_rate, self.indexes)
        else:
            return sol


sol = GA(max_iter = 100).solve(length = 15)
print(sol, sol.fitness)