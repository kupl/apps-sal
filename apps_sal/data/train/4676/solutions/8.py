def diff(poly):
    n = len(poly) - 1
    return [a * (n - i) for (i, a) in enumerate(poly[:-1])]
