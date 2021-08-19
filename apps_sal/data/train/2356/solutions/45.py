(n, k) = map(int, input().split())
mod = 998244353
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[1][1] = 1
for i in range(2, n + 1):
    for j in range(i, 0, -1):
        if 2 * j <= i:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i][2 * j]) % mod
        else:
            dp[i][j] = dp[i - 1][j - 1] % mod
print(dp[n][k])
