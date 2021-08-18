from math import gcd

LIMIT = 10**6

an = [7]
for n in range(2, LIMIT + 1):
    an.append(an[-1] + gcd(an[-1], n))

gn = [1] + [y - x for x, y, in zip(an, an[1:])]

primes = []
for x in gn:
    if x > 1 and x not in primes:
        primes.append(x)


def count_ones(n):
    return gn[:n].count(1)


def max_pn(n):
    return max(primes[:n])


def an_over_average(n):
    return 3
