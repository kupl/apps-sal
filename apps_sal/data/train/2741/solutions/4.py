def russian_peasant_multiplication(x, y):
    p = 0
    while y:
        p, x, y = p + (x if y % 2 else 0), x + x, y // 2
    return p
