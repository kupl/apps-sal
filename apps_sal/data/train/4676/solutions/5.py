def diff(poly):
    return [i * x for i, x in enumerate(poly[::-1][1:], 1)][::-1]

