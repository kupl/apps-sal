(N, K) = map(int, input().split())
MOD = 998244353
dp = [[0] * (2 * N + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    for j in range(N, 0, -1):
        if i < j:
            continue
        dp[i][j] += dp[i - 1][j - 1] + dp[i][2 * j]
        dp[i][j] %= MOD
print(dp[N][K])
