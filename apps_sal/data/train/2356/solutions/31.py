MOD = 998244353
INF = float('inf')
(N, K) = map(int, input().split())
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    for j in reversed(range(1, N + 1)):
        dp[i][j] = dp[i - 1][j - 1]
        if j * 2 <= N:
            dp[i][j] = (dp[i][j] + dp[i][2 * j]) % MOD
print(dp[N][K])
