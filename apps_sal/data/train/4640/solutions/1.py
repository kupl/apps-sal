def int_diff(l, n): return sum(n == abs(a - b)for i, a in enumerate(l)for b in l[:i])
