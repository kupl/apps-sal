def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def smallest(n):
    p = 1

    for i in range(2, n + 1):
        p *= (i / gcd(p, i))

    return p
