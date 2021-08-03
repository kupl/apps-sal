from math import *
import math


def r1(t):
    return t(input())


def r2(t):
    return [t(i) for i in input().split()]


for zzz in range(r1(int)):
    n = r1(int)
    s = r2(int)
    s.sort()
    ans = s[-1] - s[0]
    for i in range(n - 1):
        ans = min(ans, s[i + 1] - s[i])
    print(ans)
