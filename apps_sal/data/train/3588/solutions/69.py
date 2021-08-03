def quadratic(x1, x2):
    a = 1
    if x1 != x2:
        b = (x2**2 - x1**2) / (x1 - x2)
        c = -x1**2 - b * x1
    else:
        b = -2 * x1
        c = -x1**2 - b * x1
    return (a, b, c)
