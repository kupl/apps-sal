from itertools import combinations_with_replacement


def generate_pairs(n):
    return [list(a) for a in combinations_with_replacement(range(n + 1), 2)]

