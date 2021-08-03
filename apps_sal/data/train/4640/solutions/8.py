def int_diff(a, n): return a.sort() or sum(x - y == n for i, x in enumerate(a)for y in a[:i])
