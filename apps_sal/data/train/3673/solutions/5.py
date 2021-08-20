def prod(a, s=1):
    for p in a:
        s *= p
    return s


def prime_factors(n):
    for d in range(2, int(n ** 0.5) + 1):
        while n % d == 0:
            yield d
            n //= d
    if n > 1:
        yield n


def totient(n):
    if type(n) is not int or n < 0:
        return 0
    return round(n * prod((1 - 1 / p for p in set(prime_factors(n)))))
