from itertools import combinations


def find_a_b(numbers, c):
    return next(([a, b] for a, b in combinations(numbers, 2) if a * b == c), None)
