mod = 10 ** 9 + 7
table = [[0 for i in range(401)] for j in range(401)]
for i in range(401):
    S = 0
    for j in range(1, 401):
        S += pow(j, i, mod)
        S %= mod
        table[i][j] = S
(N, C) = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [[0 for i in range(C + 1)] for j in range(N)]
for i in range(C + 1):
    dp[0][i] = table[i][B[0]] - table[i][A[0] - 1]
    dp[0][i] %= mod
for i in range(1, N):
    for j in range(C + 1):
        dp[i][j] = sum((dp[i - 1][j - k] * (table[k][B[i]] - table[k][A[i] - 1]) for k in range(j + 1)))
        dp[i][j] %= mod
print(dp[N - 1][C])
