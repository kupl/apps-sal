from itertools import cycle, groupby


def trailing_zeros(num, base):
    return min((exponent(num, p) // len(list(g)) for (p, g) in groupby(factor(base))))


def exponent(n, p):
    e = 0
    while n > 0:
        n //= p
        e += n
    return e


def factor(n):
    if n < 1:
        raise ValueError('factor: n must be > 0')
    for d in [2, 3, 5]:
        while n % d == 0:
            yield d
            n = n // d
    d = 7
    wheel = cycle([4, 2, 4, 2, 4, 6, 2, 6])
    while n > 1 and d * d <= n:
        if n % d == 0:
            yield d
            n = n // d
        else:
            d += next(wheel)
    if n > 1:
        yield n
