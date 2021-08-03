n, c = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mod = 10**9 + 7

ex400 = [[1] * 401 for _ in range(401)]
for i in range(2, 401):
    for j in range(1, 401):
        ex400[i][j] = (ex400[i][j - 1] * i) % mod

cumsum400 = [[1] * 401 for _ in range(401)]
for i in range(1, 401):
    for j in range(401):
        cumsum400[i][j] = (cumsum400[i - 1][j] + ex400[i][j]) % mod

dp = [[0] * (c + 1) for _ in range(n + 1)]
dp[0][0] = 1


for i in range(1, n + 1):
    for j in range(c + 1):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][j - k] * (cumsum400[b[i - 1]][k] - cumsum400[a[i - 1] - 1][k])
            dp[i][j] %= mod

print(dp[-1][-1])
