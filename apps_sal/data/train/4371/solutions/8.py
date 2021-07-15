from itertools import combinations

def digits(num):
    lst = list(map(int, str(num)))
    return [a + b for a, b in combinations(lst, 2)]
