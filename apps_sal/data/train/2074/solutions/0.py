INF = 10 ** 18 + 179
[n, k], a = [list(map(int, input().split())) for x in range(2)]
a.sort()
dp, l = [[0] * (k - n % k + 1) for x in range(n % k + 1)], n // k
for i in range(n % k + 1):
    for j in range(k - n % k + 1):
        pos = i * (l + 1) + j * l
        dp[i][j] = min((dp[i - 1][j] + a[pos - 1] - a[pos - l - 1] if i else INF), \
                       (dp[i][j - 1] + a[pos - 1] - a[pos - l] if j else INF)) if (i or j) else 0
print(dp[n % k][k - n % k])

