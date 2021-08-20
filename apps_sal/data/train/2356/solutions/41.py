(n, k) = map(int, input().split())
MOD = 998244353
dp = [[0] * (n + 1) for i in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(1, n + 1)[::-1]:
        dp[i + 1][j] += dp[i][j - 1]
        if 2 * j <= n:
            dp[i + 1][j] += dp[i + 1][2 * j]
        dp[i + 1][j] %= MOD
print(dp[n][k] % MOD)
