from collections import Counter as cc
import sys
def input(): return sys.stdin.readline().rstrip("\r\n")


def inp(): return list(map(int, sys.stdin.readline().rstrip("\r\n").split()))


mod = 10**9 + 7
md = 998244353
tc = 1
tc, = inp()
for _ in range(tc):
    n, = inp()
    print(1 if any([int(i) % 2 == 0 for i in str(n)]) else 0)
