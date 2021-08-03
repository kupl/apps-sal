import math


def am_i_wilson(n):
    wilson_primes = [5, 13, 563]
    return True if n in wilson_primes else False
