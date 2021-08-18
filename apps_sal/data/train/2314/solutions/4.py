import sys
import os


def read_int(): return int(input())
def read_ints(): return list(map(int, input().split()))


n = read_int()
a = read_ints()
dp = [[0] * n for _ in range(n)]
f = [[0] * n for _ in range(n)]
for i in range(n - 1, -1, -1):
    f[i][i] = a[i]
    for j in range(i + 1, n):
        f[i][j] = f[i][j - 1] ^ f[i + 1][j]
for i in range(n - 1, -1, -1):
    dp[i][i] = f[i][i]
    for j in range(i + 1, n):
        dp[i][j] = max(f[i][j], dp[i][j - 1], dp[i + 1][j])
q = read_int()
for _ in range(q):
    l, r = read_ints()
    print(dp[l - 1][r - 1])
