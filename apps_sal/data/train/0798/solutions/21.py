# cook your dish here
import numpy as np
n, m = map(int, input().split())
dp = np.zeros((n, n))
forest = np.zeros((n, n))
for i in range(n):
    forest[i] = list(map(int, input().split()))
for i in range(m):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(0, z + 1):
        dp[max(x - i, 0)][max(y - (z - i), 0):min(y + (z - i) + 1, n)] = 1
        dp[min(x + i, n - 1)][max(y - (z - i), 0):min(y + (z - i) + 1, n)] = 1
for i in range(n):
    for j in range(n):
        if dp[i][j] != 1:
            forest[i][j] = -np.inf
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if j == n - 1:
            if i == n - 1:
                dp[i][j] = forest[i][j]
            else:
                dp[i][j] = forest[i][j] + dp[i + 1][j]
        elif i == n - 1:
            dp[i][j] = forest[i][j] + dp[i][j + 1]
        else:
            dp[i][j] = forest[i][j] + max(dp[i + 1][j], dp[i][j + 1])
if dp[0][0] > -np.inf:
    print("YES")
    print(int(dp[0][0]))
else:
    print("NO")
