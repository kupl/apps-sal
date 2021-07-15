import sys
input=sys.stdin.readline
R = lambda: map(int, input().split())
n, m = R()
g = [list() for i in range(n)]
for i in range(n):
    g[i] = list(R())
dp1, dp2, dp3, dp4 = ([[0] * (m + 1) for j in range(n + 1)] for i in range(4))
for i in range(n):
    for j in range(m):
        dp1[i][j] = g[i][j] + max(dp1[i - 1][j], dp1[i][j - 1])
    for j in range(m - 1, -1, -1):
        dp2[i][j] = g[i][j] + max(dp2[i - 1][j], dp2[i][j + 1])
for i in range(n - 1, -1, -1):
    for j in range(m):
        dp3[i][j] = g[i][j] + max(dp3[i + 1][j], dp3[i][j - 1])
    for j in range(m - 1, -1, -1):
        dp4[i][j] = g[i][j] + max(dp4[i + 1][j], dp4[i][j + 1])
print(max(max(dp1[i][j - 1] + dp2[i - 1][j] + dp3[i + 1][j] + dp4[i][j + 1], dp1[i - 1][j] + dp2[i][j + 1] + dp3[i][j - 1] + dp4[i + 1][j]) for j in range(1, m - 1) for i in range(1, n - 1)))
