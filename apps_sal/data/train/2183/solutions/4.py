from collections import defaultdict as dc
'''from collections import deque as dq
from bisect import bisect_left,bisect_right,insort_left'''
import sys
import math
mod = 10**9 + 7


def bs(a, x):
    i = bisect_left(a, x)
    if i != len(a):
        return i
    else:
        return len(a)


def bs(a, b):
    l = a
    r = b + 1
    x = b
    ans = 0
    while(l < r):
        mid = (l + r) // 2
        if x | mid > ans:
            ans = x | mid
            l = mid + 1
        else:
            r = mid
    return ans


def digit(n):
    a = []
    while(n > 0):
        a.append(n % 10)
        n = n // 10
    return a


def inp():
    p = int(input())
    return p


def line():
    p = list(map(int, input().split()))
    return p


def ans(a, p, z, t):
    q = []
    for i in range(len(a)):
        if p[a[i]] == t and z > 0 and p[a[i][::-1]] == 0:
            q.append(i + 1)
            z = z - 1
    return q


for i in range(inp()):
    x = inp()
    s = str(input())
    n = len(s)
    p = n
    for i in range(1, x + 1):
        if s[i - 1] != '1':
            p = (p % mod + ((p - i) % mod * (int(s[i - 1]) - 1) % mod) % mod) % mod
            if len(s) < x:
                z = s[i:]
                s = s + z * (int(s[i - 1]) - 1)
    print(p)
