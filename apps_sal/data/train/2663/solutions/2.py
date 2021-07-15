def addsup(a, b, t):
    t = set(t)
    return [[m, n, m+n] for m in a for n in b if m + n in t]
