MOD = 998244353
(n, k) = map(int, input().split())
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
dp[1][1] = 1
for i in range(2, n + 1):
    for j in range(i, 0, -1):
        dp[i][j] = dp[i - 1][j - 1]
        if 2 * j <= i:
            dp[i][j] += dp[i][2 * j]
            dp[i][j] %= MOD
print(dp[n][k])
