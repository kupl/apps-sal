import math
from itertools import count
from collections import Counter

# Prime generator based on https://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python/10733621#10733621


def genPrimes():
    # initial primes
    yield from [2, 3, 5]
    gen = genPrimes()
    """Store count generators starting from the next base prime's square
    incrementing by two times the last prime number. This is for tracking the multiples."""
    mults_set = {}
    prime = next(gen)
    prime_sq = prime ** 2
    for i in count(3, 2):
        # if i is a multiple of a prime...
        if i in mults_set:
            mults = mults_set.pop(i)

        # if i is the next prime...
        elif i < prime_sq:
            yield i
            continue

        # else i is the next primes square
        else:
            mults = count(prime_sq + 2 * prime, 2 * prime)
            prime = next(gen)
            prime_sq = prime ** 2

        # get the next multiple that isnt already in the set
        for mult in mults:
            if mult not in mults_set:
                break

        mults_set[mult] = mults


def primeFactors(n):
    # track count of prime
    output = Counter()
    rem_n = n
    """Continue dividing n by it's smallest prime factor, adding each
    factor to the Counter."""
    while rem_n > 1:
        # continue generating primes until one that can divide n is reached
        for prime in genPrimes():
            if rem_n % prime == 0:
                output[prime] += 1
                rem_n /= prime
                break

    return "".join(f"({prime}**{count})" if count > 1 else f"({prime})" for prime, count in output.items())
