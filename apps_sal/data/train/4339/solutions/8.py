def roots(a, b, c):
    return round(-(b / (2 * a)) * 2, 2) if b ** 2 - 4 * a * c >= 0 else None
