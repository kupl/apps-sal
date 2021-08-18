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
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            a[i][j] = a[i][j - 1] + 1
        for j in range(i - 1, -1, -1):
            a[i][j] = a[i][j + 1] + 1
    for i in a:
        print(*i, sep="")
