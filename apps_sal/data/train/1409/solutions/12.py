# cook your dish here
from fractions import Fraction
from collections import Counter
import string
import math
import sys
# sys.setrecursionlimit(10**6)


def isprime(x):

    # check for numbers from 2
    # to sqrt(x) if it is divisible
    # return false
    i = 2
    while(i * i <= x):
        if (x % i == 0):
            return 0
        i += 1
    return 1


def isSumOfKprimes(N, K):

    # N < 2K directly return false
    if (N < 2 * K):
        return 0

    # If K = 1 return value depends
    # on primality of N
    if (K == 1):
        return isprime(N)

    if (K == 2):

        # if N is even directly
        # return true;
        if (N % 2 == 0):
            return 1

        # If N is odd, then one
        # prime must be 2. All
        # other primes are odd
        # and cannot have a pair
        # sum as even.
        return isprime(N - 2)

    # If K >= 3 return true;
    return 1


def array_int():
    return [int(i) for i in sys.stdin.readline().split()]


def vary(arrber_of_variables):
    if arrber_of_variables == 1:
        return int(sys.stdin.readline())
    if arrber_of_variables >= 2:
        return list(map(int, sys.stdin.readline().split()))


def makedict(var):
    return dict(Counter(var))


testcases = vary(1)

for _ in range(testcases):
    n = vary(1)
    print(bin(n)[2:].count('1'))
