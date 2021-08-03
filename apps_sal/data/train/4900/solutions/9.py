def f(z, eps):
    if abs(z) >= 1:
        return -1

    n = 1
    while abs(z**n) > eps:
        n += 1

    return n
