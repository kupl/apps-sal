def diff(poly):
    return [poly[i] * (len(poly) - i - 1) for i in range(len(poly) - 1)]
