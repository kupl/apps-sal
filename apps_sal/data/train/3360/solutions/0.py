from functools import reduce
def get_chance(n, x, a):
    return round(reduce(lambda m, b: m * (1 - x / (n - b)), range(a), 1), 2)
