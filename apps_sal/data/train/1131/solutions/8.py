from collections import Counter as cc
import sys


def input():
    return sys.stdin.readline().rstrip('\r\n')


def inp():
    return list(map(int, sys.stdin.readline().rstrip('\r\n').split()))


mod = 10 ** 9 + 7
md = 998244353
tc = 1
(tc,) = inp()
for _ in range(tc):
    (n, k) = inp()
    a = inp()
    b = cc(a)
    ans = []
    for i in b.keys():
        if b[i] > k:
            ans.append(i)
    ans.sort()
    print(*ans)
