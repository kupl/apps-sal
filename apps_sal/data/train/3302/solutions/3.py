from itertools import combinations


def strings_crossover(arr, result):
    return sum((all((a == b or a == c for (a, b, c) in zip(result, *xs))) for xs in combinations(arr, 2)))
