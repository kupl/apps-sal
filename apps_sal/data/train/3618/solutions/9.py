def socialist_distribution(population, minimum):
    if sum(population) < (minimum * len(population)):
        return []
    if min(population) >= minimum:
        return population
    population[population.index(max(population))] -= 1
    population[population.index(min(population))] += 1
    return socialist_distribution(population, minimum)
