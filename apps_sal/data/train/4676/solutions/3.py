def diff(poly):
    return [i * n for (i, n) in enumerate(poly[-2::-1], 1)][::-1]
