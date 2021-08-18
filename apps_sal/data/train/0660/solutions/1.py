from fractions import Fraction
from collections import Counter
import string
import math
import sys


def isprime(x):

    i = 2
    while(i * i <= x):
        if (x % i == 0):
            return 0
        i += 1
    return 1


def isSumOfKprimes(N, K):

    if (N < 2 * K):
        return 0

    if (K == 1):
        return isprime(N)

    if (K == 2):

        if (N % 2 == 0):
            return 1

        return isprime(N - 2)

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
fact = [1 for i in range(11)]
for i in range(1, 10):
    fact[i] = fact[i - 1] * i
for _ in range(testcases):
    n = vary(1)
    p = n
    ans = 0
    if n == 0:
        print(0)
        continue
    while n > 0:
        x = n % 10
        ans += fact[x]
        n //= 10
    if p == ans:
        print(1)
    else:
        print(0)
