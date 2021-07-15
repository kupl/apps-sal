def f(z, eps, n=1):
    if abs(z) >= 1: return -1
    while abs(z ** n) >= eps: n += 1
    return n
