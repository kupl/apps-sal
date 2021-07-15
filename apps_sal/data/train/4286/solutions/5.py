from itertools import chain, count


def is_prime(n):
    return n == 2 or (n > 2 and n % 2 and all(n % i for i in range(3, int(n**0.5)+1, 2)))


def solve(n):
    deltas = chain([0], chain.from_iterable([-i, +i] for i in count(1)))
    return next(n+delta for delta in deltas if is_prime(n+delta))
