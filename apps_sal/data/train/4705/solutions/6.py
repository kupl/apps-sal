import itertools


def find_a_b(numbers, c):
    return next(([a, b] for (a, b) in itertools.combinations(numbers, 2) if a * b == c), None)
