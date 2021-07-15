def quadratic(x1, x2):
    if x1 == 0:
        return (1, -x2, 0)
    else:
        return (1, -(x1+x2), (x2*x1))

