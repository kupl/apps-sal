def quadratic(x1, x2):
    if x1 != x2:
        c = (x1 * x1 * x2 - x2 * x2 * x1) / (x1 - x2)
        b = (-c - x1 * x1) / x1 if x1 else (-c - x2 * x2) / x2
        return (1, b, c)
    else:
        return (1, -2 * x1, x1 * x1)
