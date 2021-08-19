import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


(n, m) = mints()
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
'\nfor i in range(1,n):\n\tdp1[i][0] = dp1[i-1][0] + a[i][0] # >>>>\nfor i in range(n-2,-1,-1):\n\tdp2[i][m-1] = dp2[i+1][m-1] + a[i][m-1] # <<<<\nfor i in range(n-2,-1,-1):\n\tdp3[i][0] = dp3[i+1][0] + a[i][0] # <<<<\nfor i in range(1,n):\n\tdp4[i][m-1] = dp4[i-1][m-1] + a[i][m-1] # >>>>\nfor i in range(1,m):\n\tdp1[0][i] = dp1[0][i-1] + a[0][i] # >>>>\nfor i in range(m-2,-1,-1):\n\tdp2[n-1][i] = dp2[n-1][i+1] + a[n-1][i] # <<<<\nfor i in range(1,m):\n\tdp3[n-1][i] = dp3[n-1][i-1] + a[n-1][i] # >>>>\nfor i in range(m-2,-1,-1):\n\tdp4[0][i] = dp4[0][i+1] + a[0][i] # >>>>\n'
for i in range(0, n):
    for j in range(0, m):
        z = 0
        if i - 1 >= 0:
            z = dp1[i - 1][j]
        if j - 1 >= 0:
            z = max(z, dp1[i][j - 1])
        dp1[i][j] = z + a[i][j]
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        z = 0
        if i + 1 < n:
            z = dp2[i + 1][j]
        if j + 1 < m:
            z = max(z, dp2[i][j + 1])
        dp2[i][j] = z + a[i][j]
for i in range(n - 1, -1, -1):
    for j in range(0, m):
        z = 0
        if i + 1 < n:
            z = dp3[i + 1][j]
        if j - 1 >= 0:
            z = max(z, dp3[i][j - 1])
        dp3[i][j] = z + a[i][j]
for i in range(0, n):
    for j in range(m - 1, -1, -1):
        z = 0
        if i - 1 >= 0:
            z = dp4[i - 1][j]
        if j + 1 < m:
            z = max(z, dp4[i][j + 1])
        dp4[i][j] = z + a[i][j]
'for i in dp1:\n\tprint(i)\nprint()\nfor i in dp2:\n\tprint(i)\nprint()\nfor i in dp3:\n\tprint(i)\nprint()\nfor i in dp4:\n\tprint(i)\nprint()\n'
r = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        r = max(r, dp1[i - 1][j] + dp2[i + 1][j] + dp3[i][j - 1] + dp4[i][j + 1])
        r = max(r, dp1[i][j - 1] + dp2[i][j + 1] + dp3[i + 1][j] + dp4[i - 1][j])
print(r)
