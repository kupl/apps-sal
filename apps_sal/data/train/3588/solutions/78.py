def quadratic(x1, x2):
    d = (x1 + x2)**2 - 4 * x1 * x2
    c = x1 * x2
    b = -1 * (x1 + x2)
    return(1, b, c)
