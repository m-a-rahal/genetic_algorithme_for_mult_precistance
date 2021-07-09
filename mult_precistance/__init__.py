import random
from datetime import datetime
random.seed(datetime.now())
from collections import deque


def percistance(n):
    k = 0
    while True:
        digits = str(n)
        if len(digits) == 1:
            return k
        digits = [int(x) for x in digits]
        p = 1
        for d in digits:
            p *= d
        n = p
        k += 1

    
class Population():
    def __init__(self, size, solution_length):
        self.size = size
        self._elements = [Solution.random(solution_length) for i in range(self.size)]

    def __setitem__(self, index, value):
        self._elements[index] = value

    def __getitem__(self, index):
        return self._elements[index]

    def sort(self, key):
        self._elements.sort(key=key)

    def add(self, elt):
        self._elements.append(elt)

    def reduce_to_size(self):
        self.sort(key= lambda s : -s.fitness * (1 - random.random()/9))
        self._elements = self._elements[:self.size]

    def __len__(self):
        return self.size

class Weighed_random:
    def __init__(self, weighs):
        self.weighs = weighs
        self.total = sum(w for w in weighs)
    
    def random(self):
        r = random.random()*self.total + 1 
        for i, weight in enumerate(self.weighs):
            r -= weight
            if r <= 0: return i
        return len(self.weighs) - 1    

def weighted_random(weighs):
    total = sum(w for w in weighs)
    r = random.random()*total + 1 
    for i,weight in enumerate(weighs):
        r -= weight
        if r <= 0: return i
    return len(weighs) - 1


class Solution():
        def __init__(self, x):
            self._x = x
            self.size = len(x)
            self.fitness = percistance(self.get_sol())
        @staticmethod
        def random(length):
            return Solution([random.randint(0,9) for i in range(length)])
        @property
        def x(self):
            return self._x
        @x.setter
        def x(self, value):
            self._x = value
            self.fitness = percistance(value)

        def __setitem__(self, index, value):
            self._x[index] = value

        def __getitem__(self, index):
            return self._x[index]

        def get_sol(self):
            return int(''.join([str(i) for i in self._x]))

        def mutate(self, mutation_rate, indexes):
            random.shuffle(indexes)
            for i in range(random.randint(1,int(self.size*mutation_rate))):
                self._x[indexes[i]] = random.randint(0,9)
            self.fitness = percistance(self.get_sol())
            return self

        def __len__(self):
            return self.size

        def __str__(self):
            return str(self.get_sol())

if __name__ == '__main__':
    pass
            