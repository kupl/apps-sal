def roots(a,b,c):
    import math
    d = b ** 2 - 4 * a * c
    if d > 0:
        return round(-2 * b / (2 * a), 2)
    elif d == 0:
        x = -b / (2 * a)
        return x * 2
    else:
        return None
