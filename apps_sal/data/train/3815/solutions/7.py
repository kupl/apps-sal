def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def coprimes(n):
    rslt = {1}
    for i in range(2, n):
        if gcd(n, i) == 1:
            rslt.add(i)
    return sorted(rslt)
