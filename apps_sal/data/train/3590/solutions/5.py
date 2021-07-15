from collections import Counter

def solve(a, b):
    return list(map(Counter(a).__getitem__, b))
