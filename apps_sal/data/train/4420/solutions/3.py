def mult_primefactor_sum(a, b):
    prime_factors = [factorize(n) for n in range(a, b + 1)]
    return [n for (n, pf) in enumerate(prime_factors, a) if len(pf) > 1 and n % sum(pf) == 0]


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


@memoize
def factorize(n):
    if n < 2:
        return []
    factors = []
    for k in (2, 3):
        while n % k == 0:
            n //= k
            factors.append(k)
    k = 5
    step = 2
    while k * k <= n:
        if n % k:
            k += step
            step = 6 - step
        else:
            n //= k
            factors.append(k)
    if n > 1:
        factors.append(n)
    return factors
