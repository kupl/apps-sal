n, k = map(int, input().split())
mod = 998244353

# decompose K into N numbers using 1,1/2,1/4,...
# O(N*K)
# recursion isn't good bc implicit stack space is O(N^2), too large
# can do O(n) space by using only two rows

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = 1

for i in range(1, n + 1):
    for j in range(i - 1, 0, -1):
        dp[i][j] = dp[i - 1][j - 1]
        dp[i][j] += dp[i][2 * j] if 2 * j <= n else 0
        dp[i][j] = dp[i][j] % mod
print(dp[n][k] % mod)
