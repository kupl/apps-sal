n, k = list(map(int, input().split()))
dp = [[0 for i in range(j + 1)] for j in range(n + 1)]
mod = 998244353
for i in range(1, n + 1):
    dp[i][i] = 1
for i in range(2, n + 1):
    for j in range(1, i):
        t = max(1, j - 1)
        while t <= i - 1:
            dp[i][j] += dp[i - 1][t]
            t = t * 2 + 1
        dp[i][j] %= mod
print((dp[n][k]))
