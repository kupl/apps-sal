from collections import OrderedDict
from math import sqrt


class OrderedIntDict(OrderedDict):
    def __missing__(self, key):
        return 0


def format_factor(n, times):
    return (
        "({n})".format(n=n) if times == 1
        else "({n}**{times})".format(n=n, times=times)
    )


def prime_factors(number):
    factors = OrderedIntDict()
    for n in range(2, int(sqrt(number))+1):
        while number % n == 0:
            number //= n
            factors[n] += 1
    if number > 1:
        factors[number] = 1
    return "".join(
        format_factor(n, times)
        for n, times in factors.items()
    )
    

primeFactors = prime_factors
