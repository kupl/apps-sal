import itertools


def solve(a, b):
    primes = set([2] + [n for n in range(3, b, 2) if all(n % r for r in range(3, int(n**0.5) + 1, 2))])
    return sum(sum(map(int, str(x * y))) in primes for x, y in itertools.combinations_with_replacement([p for p in primes if a <= p < b], 2))
