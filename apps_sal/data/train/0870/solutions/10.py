import sys
from random import randint


def rec(x, y, b):
    if x == n:
        return 0
    if y == 3:
        return n
    if dp[x][y] != -1:
        return dp[x][y]
    if y == 1:
        p = b ^ 1
    else:
        p = b
    res = n
    if a[x] != p:
        res = min(res, rec(x, y + 1, b))
        res = min(res, 1 + rec(x + 1, y, b))
    else:
        res = min(res, rec(x + 1, y, b))
    dp[x][y] = res
    return dp[x][y]


sys.setrecursionlimit(10**6)
t = int(input())
# t = 1
for _ in range(t):
    a = list(map(int, list(input())))
    # a = [randint(0, 1) for i in range(1000)]
    n = len(a)
    dp = [[-1, -1, -1] for i in range(n)]
    res = rec(0, 0, 0)
    dp = [[-1, -1, -1] for i in range(n)]
    res = min(res, rec(0, 0, 1))
    print(res)
