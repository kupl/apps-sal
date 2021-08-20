import math


def phi(a):
    res = a
    b = a
    i = 2
    while i * i <= a:
        if a % i == 0:
            res -= res // i
            while a % i == 0:
                a //= i
        i = i + 1
    if a > 1:
        res -= res // a
    return res


def inverseMod(a, m):
    if math.gcd(a, m) != 1:
        return None
    _phi = phi(m)
    return pow(a, _phi - 1, m)
