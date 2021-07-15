from itertools import combinations

def digits(num):
    ns = list(map(int, str(num)))
    return [a+b for a, b in combinations(ns, 2)]
