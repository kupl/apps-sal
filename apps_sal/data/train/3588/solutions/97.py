def quadratic(x1, x2):
    if isinstance(x1, int) and isinstance(x2, int):
        b = - (x1 + x2)
        c = x1 * x2
        return 1, b, c
    else:
        return False


print(quadratic(1, 3))
