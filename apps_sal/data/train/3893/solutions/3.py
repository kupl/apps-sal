import math


def divisors(n):
    o = [i for i in range(2, int(math.ceil(n / 2) + 1)) if n % i == 0]
    return o if len(o) > 0 else "%d is prime" % n
