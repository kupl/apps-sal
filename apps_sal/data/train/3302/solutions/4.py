from itertools import combinations


def strings_crossover(arr, result):
    return sum((all((a in b for (a, b) in zip(result, l))) for l in (zip(*c) for c in combinations(arr, 2))))
