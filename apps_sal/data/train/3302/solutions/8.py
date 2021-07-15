from itertools import combinations

def strings_crossover(arr, result):
    combs = [*combinations(arr, 2)]
    t = 0
    for k in range(len(combs)):
        x, y, z = set(enumerate(result)), set(enumerate(combs[k][0])), set(enumerate(combs[k][1]))
        t += not x - (y | z)
    return t
