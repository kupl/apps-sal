def solve(p):
    """See codewars.com kata Divisible by primes."""
    n = p - 1
    for f in factors(n):
        m = n // f
        if pow(10, m, p) == 1:
            n = m
    return '%d-altsum' % (n // 2) if n % 2 == 0 else '%d-sum' % n


def factors(n):
    m = 2
    while m * m <= n:
        while n % m == 0:
            yield m
            n //= m
        m += 1 if m == 2 else 2
    if n > 1:
        yield n

