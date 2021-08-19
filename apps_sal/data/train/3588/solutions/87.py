def quadratic(x1, x2):
    (a, b, c) = (0, -(x1 + x2), x1 * x2)
    if x1 * x2 != 0:
        a = c / (x1 * x2)
    elif x1 + x2 != 0:
        a = -b / (x1 + x2)
    return (a, b, c)
