from itertools import accumulate
(N, C) = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
mod = 10 ** 9 + 7
X = [list(accumulate([pow(x, d, mod) for x in range(401)])) for d in range(C + 1)]
dp = [[0] * (C + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    for d in range(C + 1):
        dp[i][d] = sum([dp[i - 1][d - k] * (X[k][B[i - 1]] - X[k][A[i - 1] - 1]) for k in range(d + 1)]) % mod
print(dp[-1][-1])
