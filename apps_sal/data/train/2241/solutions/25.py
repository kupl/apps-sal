mod = 10**9 + 7
N, C = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [[0] * (C + 1) for i in range(N + 1)]
dp[-1][0] = 1
S = [[0] * (C + 1) for _ in range(N + 1)]
for i in range(N):
    power = [1] * (400 + 1)
    for j in range(C + 1):
        for x in range(A[i], B[i] + 1):
            S[i][j] += power[x]
            S[i][j] %= mod
            power[x] *= x
            power[x] %= mod
for i in range(N):
    for j in range(C + 1):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][j - k] * S[i][k]
            dp[i][j] %= mod
print((dp[-2][-1]))
