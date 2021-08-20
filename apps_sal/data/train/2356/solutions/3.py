(N, K) = list(map(int, input().split()))
MOD = 998244353
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    dp[i][i] = 1
    for j in range(i - 1, 0, -1):
        if 2 * j <= i:
            dp[i][j] = dp[i - 1][j - 1] + dp[i][2 * j]
        else:
            dp[i][j] = dp[i - 1][j - 1]
        dp[i][j] %= MOD
print(dp[N][K])
