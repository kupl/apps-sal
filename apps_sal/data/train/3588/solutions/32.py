def quadratic(x1, x2):
    print((x1, x2))
    a = 1
    if x2 - x1 != 0:
        b = (x1 ** 2 - x2 ** 2) / (x2 - x1)
        c = -x1 ** 2 - b * x1
    else:
        c = x1 ** 2
        b = -2 * x1
    return (a, b, c)
