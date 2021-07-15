from random import choices
from itertools import islice, count

def squares(n):
    return [a ** 2 for a in range(1, n + 1)]

def num_range(n, start, step):
    return list(islice(count(start, step), n))

def rand_range(n, mn, mx):
    return choices(range(mn, mx + 1), k = n)

def primes(n):
    return list(islice((a for a in count(2) if all(a % b != 0 for b in range(2, 1 + int(a ** 0.5)))), n))
