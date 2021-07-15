def socialist_distribution(population, minimum):
    if len(population) * minimum > sum(population):
        return []
    
    while min(population) < minimum:
        i_max = population.index(max(population))
        i_min = population.index(min(population))
        population[i_max] -= 1
        population[i_min] += 1
    
    return population
