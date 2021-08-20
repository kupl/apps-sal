import math


def egged(year, span):
    if year == 0:
        return 'No chickens yet!'
    i = 1
    chickens = list()
    while i <= year:
        new_chickens = list()
        for chicken in chickens:
            new_chickens.append([math.floor(chicken[0] * 0.8), chicken[1] - 1])
        new_chickens.append([300, span])
        new_chickens.append([300, span])
        new_chickens.append([300, span])
        chickens = new_chickens
        total_eggs = 0
        for chicken in chickens:
            if chicken[1] > 0:
                total_eggs = total_eggs + chicken[0]
        i = i + 1
    return total_eggs
