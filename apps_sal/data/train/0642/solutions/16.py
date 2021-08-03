import sys

from sys import stdin
L, R = 1, 10**16


def ck(m):
    c = 0
    for i, x in enumerate(l):
        if c < x:
            c = x
        if x + d < c:
            return False
        c += m
    return True


def bs():
    l, r = L, R
    while l < r:
        m = (l + r + 1) // 2
        if ck(m):
            l = m
        else:
            r = m - 1
    return l


for _ in range(int(input())):
    n, d = map(int, input().split())
    d *= 10**6
    l = sorted(map(lambda x: int(x) * (10**6), sys.stdin.readline().strip().split()))
    x = bs()
    print(x / 10**6)
