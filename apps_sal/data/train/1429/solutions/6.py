from bisect import bisect_right as br
from bisect import bisect_left as bl
from collections import *
from itertools import *
import functools
import sys
from math import *
from decimal import *
from copy import *
getcontext().prec = 30
MAX = sys.maxsize
MAXN = 10 ** 6 + 10
MOD = 10 ** 9 + 7


def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def mhd(a, b):
    return abs(a[0] - b[0]) + abs(b[1] - a[1])


def numIN(x=' '):
    return map(int, sys.stdin.readline().strip().split(x))


def charIN(x=' '):
    return sys.stdin.readline().strip().split(x)


def arrIN():
    return list(numIN())


def dis(x, y):
    a = y[0] - x[0]
    b = x[1] - y[1]
    return (a * a + b * b) ** 0.5


def lgcd(a):
    g = a[0]
    for i in range(1, len(a)):
        g = math.gcd(g, a[i])
    return g


def ms(a):
    msf = -MAX
    meh = 0
    st = en = be = 0
    for i in range(len(a)):
        meh += a[i]
        if msf < meh:
            msf = meh
            st = be
            en = i
        if meh < 0:
            meh = 0
            be = i + 1
    return (msf, st, en)


def flush():
    return sys.stdout.flush()


'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\xa0\xa0\xa0\xa0'
for _ in range(int(input())):
    n = int(input())
    a = arrIN()
    p = list(map(float, input().split()))
    dp = [0] * 32
    for i in range(32):
        for j in range(n):
            if a[j] & 1 << i:
                dp[i] = (1 - p[j]) * dp[i] + (1 - dp[i]) * p[j]
    ans = 0
    for i in range(32):
        ans += dp[i] * (1 << i)
    print(ans)
