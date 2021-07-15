MOD = 998244353

n, k = map(int, input().split())
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        dp[i][j] = dp[i - 1][j - 1]
        try:
            dp[i][j] += dp[i][j * 2]
        except IndexError:
            pass
        dp[i][j] %= MOD

print(dp[n][k])
