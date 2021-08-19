def solve(a, b):
    return [2, 1][any((a.count(e) > 1 for e in a if e not in b))]
