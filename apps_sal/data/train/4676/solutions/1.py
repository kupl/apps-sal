def diff(poly):
    return [d * c for d, c in enumerate(poly[::-1]) if d][::-1]
