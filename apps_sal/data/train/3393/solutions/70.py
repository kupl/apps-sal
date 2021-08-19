import math


def list_squared(m, n):
    p = []
    for x in range(m, n + 1):
        ds = sum((y ** 2 + (x / y) ** 2 for y in range(2, math.ceil(math.sqrt(x))) if x % y == 0)) + x ** 2
        if x > 1:
            ds += 1
            if x % math.sqrt(x) == 0:
                ds += x
        if math.sqrt(ds).is_integer():
            p = p + [[x, ds]]
    return p
