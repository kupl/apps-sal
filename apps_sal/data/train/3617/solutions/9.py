def is_zero_balanced(a):
    p = sorted(abs(e) for e in a if e > 0)
    n = sorted(abs(e) for e in a if e < 0)
    return all(x == y for x, y in zip(p, n)) and len(p) == len(n) and len(a) > 0
