from itertools import combinations


def strings_crossover(arr, result):
    return sum(all(x == z or y == z for x, y, z in zip(a, b, result)) for a, b in combinations(arr, 2))
