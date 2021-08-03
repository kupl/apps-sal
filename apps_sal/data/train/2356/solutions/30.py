N, K = map(int, input().split())
dp = [[0] * (N + 2) for i in range(N + 1)]

for i in range(1, N + 1):
    dp[i][i] = 1
    for j in range(i - 1, 0, -1):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i][min(2 * j, N + 1)]) % 998244353

print(dp[N][K])
