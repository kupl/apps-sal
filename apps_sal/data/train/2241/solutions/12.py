from itertools import accumulate
import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7
(n, c) = map(int, input().split())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
E = [[0] * (c + 1) for _ in range(n)]
for j in range(c + 1):
    cumsum = tuple((pow(k, j, MOD) for k in range(401)))
    cumsum = tuple((i % MOD for i in accumulate(cumsum)))
    for (i, (a, b)) in enumerate(zip(A, B)):
        E[i][j] = cumsum[b] - cumsum[a - 1]
dp = [[0] * (c + 1) for _ in range(n + 1)]
dp[0][0] = 1
for (i, e) in enumerate(E):
    for (j, f) in enumerate(e):
        for k in range(c + 1):
            if j + k <= c:
                dp[i + 1][j + k] += dp[i][k] * f
                dp[i + 1][j + k] %= MOD
ans = dp[n][c]
print(ans)
