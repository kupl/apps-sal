(n, k) = map(int, input().split())
mod = 998244353
dp = [[0] * 6005 for _ in range(3001)]
dp[0][0] = 1
for i in range(1, 3001):
    for j in range(i, 0, -1):
        dp[i][j] = dp[i - 1][j - 1] + dp[i][2 * j]
        dp[i][j] %= mod
ans = dp[n][k]
print(ans)
