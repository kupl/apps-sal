def min_sum(a): return a.sort() or sum(x * y for x, y in zip(a, a[::-1])) / 2
