import math
import collections
import os
import sys
from io import BytesIO, IOBase


def ii():
    return int(input())


def si():
    return input()


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


def CountFrequency(arr):
    return collections.Counter(arr)


for i in range(1):
    (n, q) = mi()
    p = pow(2, n + 1) - 2
    t = 1
    b = pow(2, n)
    s = n + 1
    for i in range(q):
        a = li()
        if len(a) == 2:
            if a[1] == 1 or a[1] == 2:
                p *= 2
                p += s
                t *= 2
                b *= 2
            else:
                p *= 2
                if a[1] == 3:
                    p += t
                    t = b
                    s *= 2
                else:
                    p += b
                    b = t
                    s *= 2
        else:
            print(p % 1000000007)
