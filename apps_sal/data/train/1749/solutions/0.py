def isqrt(num):
    """Compute int(sqrt(n)) for n integer > 0
    O(log4(n)) and no floating point operation, no division"""
    (res, bit) = (0, 1)
    while bit <= num:
        bit <<= 2
    bit >>= 2
    while bit:
        if num >= res + bit:
            num -= res + bit
            res += bit << 1
        res >>= 1
        bit >>= 2
    return res


def factorize(n):
    for q in (2, 3):
        m = 0
        while not n % q:
            m += 1
            n //= q
        if m:
            yield (q, m)
    (m, d, q, maxq) = (0, 4, 1, isqrt(n))
    while q <= maxq:
        (q, d) = (q + d, 6 - d)
        while not n % q:
            m += 1
            n //= q
        if m:
            yield (q, m)
            (m, d, q, maxq) = (0, 4, 1, isqrt(n))
    if n > 1:
        yield (n, 1)


def count_factor(n, f):
    s = 0
    while n >= f:
        n //= f
        s += n
    return s


def trailing_zeros(n, b):
    return min((count_factor(n, f) // m for (f, m) in factorize(b)))
