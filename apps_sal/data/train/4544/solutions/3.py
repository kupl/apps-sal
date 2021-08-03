from collections import Counter


def factors(n):
    c = Counter()
    d = 2
    while d * d <= n:
        while n % d == 0:
            n //= d
            c[d] += 1
        d += 1 + (d > 2)
    if n > 1:
        c[n] += 1
    return c


def factor_sum(n):
    while True:
        c = factors(n)
        result = sum(key * value for key, value in c.items())
        if result == n:
            return n
        n = result
