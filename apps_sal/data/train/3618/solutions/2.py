def socialist_distribution(pop, minimum):
    if minimum > sum(pop)//len(pop):
        return []
    while min(pop) < minimum:
        pop[pop.index(min(pop))] += 1
        pop[pop.index(max(pop))] -= 1
    return pop
