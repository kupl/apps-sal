def solve(a): return [j for i, j in enumerate(a) if a[i:].count(j) == 1]
