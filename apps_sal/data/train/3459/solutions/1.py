from itertools import combinations

def solve(n,k):
    return min((''.join(c) for c in combinations(str(n), len(str(n))-k)), key=int)
