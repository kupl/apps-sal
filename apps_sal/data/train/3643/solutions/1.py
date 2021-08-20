def distribute(n, w):
    (g, (d, r)) = (iter(range(w)), divmod(w, n))
    return [[next(g) for _ in range(d + (i < r))] for i in range(n)]
