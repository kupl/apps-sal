def quadratic(x1, x2):
    if x1 == x2:
        return (1, int(-2 * x1), int(x1 ** 2))
    else:
        b = (x1 ** 2 - x2 ** 2) / (x2 - x1)
        return (1, int(b), int(-1 * (x1 ** 2) - b * x1))

