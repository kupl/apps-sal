from bisect import bisect_right as br
from bisect import bisect_left as bl
from collections import defaultdict
from itertools import combinations
import functools
import sys
import math
MAX = sys.maxsize
MAXN = 10**6 + 10
MOD = 10**9 + 7


def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def mhd(a, b, x, y):
    return abs(a - x) + abs(b - y)


def numIN():
    return(map(int, sys.stdin.readline().strip().split()))


def charIN():
    return(sys.stdin.readline().strip().split())


t = [0] * 1000010


def create(a, n):
    global t
    for i in range(n, 2 * n):
        t[i] = a[i - n]
    for i in range(n - 1, 0, -1):
        t[i] = t[2 * i] + t[2 * i + 1]


def cal(n, k):
    res = 1
    c = [0] * (k + 1)
    c[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            c[j] = (c[j] + c[j - 1]) % MOD
    return c[k]


for i in range(int(input())):
    n = int(input())
    a = str(n)
    l = len(a)
    ans = n
    p1 = pow(10, l, MOD)
    p2 = pow(10, l - 1, MOD)
    for j in range(l - 1):
        n -= (int(a[j]) * p2)
        n %= MOD
        n *= 10
        n %= MOD
        n += int(a[j])
        n %= MOD
        ans *= p1
        ans %= MOD
        ans += n
        ans %= MOD

    print(ans)
