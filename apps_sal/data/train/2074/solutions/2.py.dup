inf = 10 ** 10
n, k = list(map(int, input().split()))
a = sorted(map(int, input().split()))
L, M = n // k, n % k
dp = [[0] * (k - M + 1) for i in range(M + 1)]
for i in range(M + 1):
    for j in range(k - M + 1):
        pos = i * (L + 1) + j * L
        dp[i][j] = min((dp[i - 1][j] + a[pos - 1] - a[pos - L - 1] if i else inf),
                       (dp[i][j - 1] + a[pos - 1] - a[pos - L] if j else inf)) if (i or j) else 0
print(dp[M][k - M])
