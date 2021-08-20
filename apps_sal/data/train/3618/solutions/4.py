def socialist_distribution(population, minimum):
    if sum(population) < minimum * len(population):
        return []
    population = population[:]
    for _ in range(sum((max(minimum - p, 0) for p in population))):
        population[min(range(len(population)), key=population.__getitem__)] += 1
        population[max(range(len(population)), key=population.__getitem__)] -= 1
    return population
