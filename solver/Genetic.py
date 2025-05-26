import random

class GeneticSolver:
    def __init__(self, size, population=100, max_iters=1000):
        self.size = size
        self.population_size = population
        self.iterations = max_iters

    def score(self, chromosome):
        conflict_count = 0
        for a in range(self.size):
            for b in range(a + 1, self.size):
                if abs(chromosome[a] - chromosome[b]) == abs(a - b):
                    conflict_count += 1
        return -conflict_count

    def breed(self, parent1, parent2):
        cross_point = random.randint(1, self.size - 2)
        return parent1[:cross_point] + parent2[cross_point:]

    def random_change(self, chromosome, chance=0.1):
        if random.random() < chance:
            idx1, idx2 = random.sample(range(self.size), 2)
            chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
        return chromosome

    def find_solution(self):
        pool = [random.sample(range(self.size), self.size) for _ in range(self.population_size)]
        for _ in range(self.iterations):
            pool.sort(key=self.score, reverse=True)
            if self.score(pool[0]) == 0:
                return pool[0]
            next_generation = pool[:10]
            while len(next_generation) < self.population_size:
                dad, mom = random.sample(pool[:50], 2)
                kid = self.breed(dad, mom)
                kid = self.random_change(kid)
                next_generation.append(kid)
            pool = next_generation
        return pool[0]
