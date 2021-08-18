from math import *


def printNcR(n, r):

    p = 1
    k = 1

    if (n - r < r):
        r = n - r

    if (r != 0):
        while (r):
            p *= n
            k *= r

            m = gcd(p, k)

            p //= m
            k //= m

            n -= 1
            r -= 1

    else:
        p = 1

    return p


n, k = map(int, input().split())
print(int(printNcR(n + k - 1, k) % (1000000000 + 7)))
