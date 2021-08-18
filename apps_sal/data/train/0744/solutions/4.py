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
    if n == 1:
        print('*')
        continue
    n = n // 2 + 1
    print('*')
    a = [' '] * (n)
    a[0] = '*'
    a[1] = '*'
    print()
    for i in range(1, n - 1):
        print('*' + ' ' * (i - 1) + '*')
        print()
    print('*' + ' ' * (n - 2) + '*')
    print()
    for i in range(n - 2, 0, -1):
        print('*' + ' ' * (i - 1) + '*')
        print()
    print('*')
