from fractions import gcd


def coprimes(n):
    ret = []
    for x in range(int(n / 2) + 1):
        if gcd(x, n - x) == 1:
            ret += [x]
            ret += [n - x]
    return sorted(set(ret))
