def f(z, eps):
    import math
    if z == 1:
        return 1
    elif abs(z) >= 1:
        return -1
    else:
        n = 1
        while abs(z)**(n) > eps:
            n += 1
        return n
