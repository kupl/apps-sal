from functools import reduce
from operator import mul

def is_smooth(n):
    num = n
    factors = [1]
    prime_fact = iter([i for i in (2,3,5,7) if not n%i])
    fact = next(prime_fact, n)
    while reduce(mul, factors) != n and fact != 0:
        if not num % fact:
            factors += [fact]
            num /= fact
        else:
            fact = next(prime_fact, 0)
    return "non-smooth" if fact==0 else "power of 2" if factors[-1] == 2 else "3-smooth" if factors[-1] == 3 else\
           "Hamming number" if factors[-1] == 5 else "humble number" if factors[-1] == 7 else "non-smooth"

