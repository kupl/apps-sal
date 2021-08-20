def diff(poly):
    return [-i * n for (i, n) in enumerate(poly[:-1], -len(poly) + 1)]
