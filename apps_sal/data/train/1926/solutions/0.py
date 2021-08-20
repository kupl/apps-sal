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
    powers = [[factor ** i for i in range(count + 1)] for (factor, count) in list(pf_with_multiplicity.items())]
    for prime_power_combo in itertools.product(*powers):
        yield prod(prime_power_combo)


class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        d1 = sorted(list(get_divisors(num + 1)))
        d2 = sorted(list(get_divisors(num + 2)))
        if len(d1) % 2 == 1:
            mid = d1[int((len(d1) - 1) / 2)]
            return [int(mid), int(mid)]
        if len(d2) % 2 == 1:
            mid = d2[int((len(d2) - 1) / 2)]
            return [int(mid), int(mid)]
        (l1, r1) = (d1[int(len(d1) / 2)], d1[int(len(d1) / 2) - 1])
        (l2, r2) = (d2[int(len(d2) / 2)], d2[int(len(d2) / 2) - 1])
        if abs(l1 - r1) < abs(l2 - r2):
            return [int(l1), int(r1)]
        else:
            return [int(l2), int(r2)]
