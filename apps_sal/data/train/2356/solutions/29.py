def MI():
    return list(map(int, input().split()))


n, k = MI()
mod = 998244353
if n < k:
    print((0))
    return

dp = [[0] * (2 * n + 1) for i in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        dp[i][j] += dp[i][j * 2] + dp[i - 1][j - 1]
        dp[i][j] %= mod

print((dp[n][k]))
