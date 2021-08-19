mod = 998244353
(N, K) = map(int, input().split())
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    for j in reversed(range(N + 1)):
        dp[i][j] = dp[i - 1][j - 1] + (dp[i][2 * j] if 2 * j <= N else 0)
        dp[i][j] %= mod
print(dp[N][K])
