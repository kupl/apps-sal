def weight(n, w):
    from math import e
    i0 = 0.14849853757254047
    an = (1 - e ** -(2 * n + 2)) / (1 - e ** -2)
    return i0 * an * w
