from itertools import product

def outcome(n, s, k):
    return sum( sum(p) == k for p in product(range(1, s+1), repeat=n) )
