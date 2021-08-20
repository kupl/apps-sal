(n, k) = map(int, input().split())
mod = 998244353
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 1
for i in range(1, n + 1):
    for j in range(i - 1, 0, -1):
        dp[i][j] = dp[i - 1][j - 1]
        dp[i][j] += dp[i][2 * j] if 2 * j <= n else 0
        dp[i][j] = dp[i][j] % mod
print(dp[n][k] % mod)
