from itertools import combinations

def solve(n, k):
    return ''.join(min(combinations(str(n), len(str(n))-k)))
