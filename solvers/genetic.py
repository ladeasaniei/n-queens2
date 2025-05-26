import random

class GeneticSolver:
    def __init__(self, n, pop_size=100, generations=1000):
        self.n = n
        self.pop_size = pop_size
        self.generations = generations

    def fitness(self, individual):
        clashes = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if abs(individual[i] - individual[j]) == abs(i - j):
                    clashes += 1
        return -clashes

    def crossover(self, parent1, parent2):
        point = random.randint(1, self.n - 2)
        return parent1[:point] + parent2[point:]

    def mutate(self, individual, rate=0.1):
        if random.random() < rate:
            i, j = random.sample(range(self.n), 2)
            individual[i], individual[j] = individual[j], individual[i]
        return individual

    def solve(self):
        population = [random.sample(range(self.n), self.n) for _ in range(self.pop_size)]
        for _ in range(self.generations):
            population.sort(key=self.fitness, reverse=True)
            if self.fitness(population[0]) == 0:
                return population[0]
            next_generation = population[:10]
            while len(next_generation) < self.pop_size:
                p1, p2 = random.sample(population[:50], 2)
                child = self.crossover(p1, p2)
                child = self.mutate(child)
                next_generation.append(child)
            population = next_generation
        return population[0]