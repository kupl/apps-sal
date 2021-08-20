def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        (g, y, x) = egcd(b % a, a)
        return (g, x - b // a * y, y)


def inverseMod(a, m):
    (g, x, y) = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m
