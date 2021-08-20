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
    (n,) = inp()
    a = [int(i) for i in str(n)]
    print('Yes' if n % sum(a) == 0 else 'No')
