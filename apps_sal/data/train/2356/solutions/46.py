mod = 998244353
(n, k) = map(int, input().split())
dp = [[0] * (n + 1) for i in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(i, -1, -1):
        if j:
            dp[i][j] += dp[i - 1][j - 1]
        if j * 2 <= i:
            dp[i][j] += dp[i][j * 2]
        dp[i][j] %= mod
print(dp[n][k])
