def socialist_distribution(population, minimum):
    if sum(population) < len(population) * minimum:
        return []
    while 1:
        poor = rich = 0
        for idx, need in enumerate(population):
            if need < population[poor]: poor = idx
            if need > population[rich]: rich = idx
        if population[poor] >= minimum:
            return population
        population[rich] -= 1
        population[poor] += 1
