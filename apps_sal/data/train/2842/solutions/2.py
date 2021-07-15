def coordinates(a, b, p = 0):
    return round(sum((i - j) ** 2 for i, j in zip(a, b)) ** 0.5, p)
