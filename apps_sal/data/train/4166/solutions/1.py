import collections
import itertools


def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n


def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result


def get_divisors(n):
    pf = prime_factors(n)

    pf_with_multiplicity = collections.Counter(pf)

    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in pf_with_multiplicity.items()
    ]

    for prime_power_combo in itertools.product(*powers):
        yield prod(prime_power_combo)


def rem(n, p):
    v = 1
    for i in range(0, n // 1000):
        v = v * (10 ** 1000)
        v = v % p
    v = v * (10 ** (n % 1000))
    v = v % p
    return v


def solve(p):
    nl = list(get_divisors(p - 1))
    nl = [int(x) for x in nl]
    nl = sorted(nl)

    for n in nl:
        if rem(n, p) == 1:
            return str(n) + '-sum'
        if rem(n, p) == p - 1:
            return str(n) + '-altsum'
