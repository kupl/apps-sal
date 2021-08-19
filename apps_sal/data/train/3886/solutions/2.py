def total(lst):
    return sum((lst[i] for i in primes_gen(len(lst))))


def primes_gen(limit):
    for current in (2, 3, 5, 7):
        if current > limit:
            return
        yield current
    composites = {}
    primes = primes_gen(limit)
    base_prime = next(primes) and next(primes)
    next_square = base_prime * base_prime
    for current in range(9, limit, 2):
        if current in composites:
            sieve = composites.pop(current)
        elif current < next_square:
            yield current
            continue
        else:
            sieve = 2 * base_prime
            base_prime = next(primes)
            next_square = base_prime * base_prime
        current += sieve
        while current in composites:
            current += sieve
        composites[current] = sieve
