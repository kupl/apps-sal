import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


n, m = mints()
a = [0] * n
dp1 = [0] * n
dp2 = [0] * n
dp3 = [0] * n
dp4 = [0] * n
for i in range(n):
    a[i] = list(mints())
    dp1[i] = [0] * m
    dp2[i] = [0] * m
    dp3[i] = [0] * m
    dp4[i] = [0] * m

dp1[0][0] = a[0][0]
dp2[n - 1][m - 1] = a[n - 1][m - 1]
dp3[n - 1][0] = a[n - 1][0]
dp4[0][m - 1] = a[0][m - 1]
for i in range(1, n):
    dp1[i][0] = dp1[i - 1][0] + a[i][0]  # >>>>
for i in range(n - 2, -1, -1):
    dp2[i][m - 1] = dp2[i + 1][m - 1] + a[i][m - 1]  # <<<<
for i in range(n - 2, -1, -1):
    dp3[i][0] = dp3[i + 1][0] + a[i][0]  # <<<<
for i in range(1, n):
    dp4[i][m - 1] = dp4[i - 1][m - 1] + a[i][m - 1]  # >>>>
for i in range(1, m):
    dp1[0][i] = dp1[0][i - 1] + a[0][i]  # >>>>
for i in range(m - 2, -1, -1):
    dp2[n - 1][i] = dp2[n - 1][i + 1] + a[n - 1][i]  # <<<<
for i in range(1, m):
    dp3[n - 1][i] = dp3[n - 1][i - 1] + a[n - 1][i]  # >>>>
for i in range(m - 2, -1, -1):
    dp4[0][i] = dp4[0][i + 1] + a[0][i]  # >>>>
for i in range(1, n):
    for j in range(1, m):
        dp1[i][j] = max(dp1[i - 1][j], dp1[i][j - 1]) + a[i][j]
for i in range(n - 2, -1, -1):
    for j in range(m - 2, -1, -1):
        dp2[i][j] = max(dp2[i + 1][j], dp2[i][j + 1]) + a[i][j]
for i in range(n - 2, -1, -1):
    for j in range(1, m):
        dp3[i][j] = max(dp3[i + 1][j], dp3[i][j - 1]) + a[i][j]
for i in range(1, n):
    for j in range(m - 2, -1, -1):
        dp4[i][j] = max(dp4[i - 1][j], dp4[i][j + 1]) + a[i][j]
r = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        r = max(r, dp1[i - 1][j] + dp2[i + 1][j] + dp3[i][j - 1] + dp4[i][j + 1])
        r = max(r, dp1[i][j - 1] + dp2[i][j + 1] + dp3[i + 1][j] + dp4[i - 1][j])
print(r)
