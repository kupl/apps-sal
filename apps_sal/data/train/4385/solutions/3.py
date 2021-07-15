from itertools import combinations_with_replacement

def generate_pairs(n, m=2):
    return list(map(list, combinations_with_replacement(range(n+1), m)))
