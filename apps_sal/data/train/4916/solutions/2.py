from itertools import zip_longest
import math


def get_primes(how_many, group_size=2):
    if how_many > 0:
        pr = primes(how_many)
        yield from [tuple(e) for e in zip_longest(*[iter(pr)] * group_size)]


def is_prime(n):
    return all((n % i for i in range(3, int(math.sqrt(n)) + 1, 2)))


def primes(n):
    (i, pr) = (3, [2])
    while n > 1:
        if is_prime(i):
            n -= 1
            pr.append(i)
        i += 2
    return pr
