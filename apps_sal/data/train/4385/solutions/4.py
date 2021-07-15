from itertools import combinations_with_replacement

def generate_pairs(n):
    return sorted(map(list, combinations_with_replacement(list(range(n + 1)), 2)))
