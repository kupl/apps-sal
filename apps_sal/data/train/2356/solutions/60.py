N, K = map(int, input().split())
M = 998244353
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    for j in range(N, 0, -1):
        dp[i][j] = dp[i - 1][j - 1]
        if 2 * j <= N:
            dp[i][j] += dp[i][2 * j]
        dp[i][j] %= M
print(dp[N][K])
