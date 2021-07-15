n, c = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mod = pow(10, 9) + 7
powlist = [[1] * 405 for _ in range(405)]
for i in range(1, 405):
    for j in range(1, 405):
        powlist[i][j] = j * powlist[i - 1][j] % mod
for i in range(405):
    for j in range(1, 405):
        powlist[i][j] += powlist[i][j - 1]
        powlist[i][j] %= mod
x = [[0] * (c + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(c + 1):
        x[i][j] = powlist[j][b[i - 1]] - powlist[j][a[i - 1] - 1]
        x[i][j] %= mod
dp = [[0] * (c + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(c + 1):
        s = 0
        for k in range(j + 1):
            s += dp[i - 1][k] * x[i][j - k]
            s %= mod
        dp[i][j] = s
ans = dp[n][c]
print(ans)
