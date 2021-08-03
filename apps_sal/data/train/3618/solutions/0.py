def socialist_distribution(population, minimum):
    if minimum > sum(population) // len(population):
        return []
    while min(population) < minimum:
        population[population.index(min(population))] += 1
        population[population.index(max(population))] -= 1
    return population
