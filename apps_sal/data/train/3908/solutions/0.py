from collections import Counter

def solve(a):
    c = Counter(a)
    return sorted(a, key=lambda k: (-c[k], k))
