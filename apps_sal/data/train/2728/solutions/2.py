def gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


def inverse_mod(a, b):
    if gcd(a, b) != 1:
        return None
    (x, y, B) = (1, 0, b)
    while a > 1:
        q = a // b
        (a, b) = (b, a % b)
        (x, y) = (y, x - q * y)
    return x + B if x < 0 else x


def inverseMod(a, b):
    return inverse_mod(a, b)
