def diff(poly):
    n = len(poly) - 1
    poly = poly[:-1]
    return [x * (n - i) for (i, x) in enumerate(poly)]
