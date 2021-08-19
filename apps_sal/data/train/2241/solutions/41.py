import numpy as np
N, C = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
mod = 10**9 + 7
P = np.empty((404, 404), dtype=np.int64)
P[0, :] = 1
ar = np.arange(404, dtype=np.int64)
for i in range(1, 404):
    P[i] = P[i - 1] * ar % mod
# この時点で  # P[i, c] = i**c % mod

P = P.cumsum(axis=1, dtype=np.int64) % mod  # P[i, c] = Σ_{k=0}^i k**c % mod
P = P.T

dp = np.zeros(C + 1, dtype=np.int64)
dp[0] = 1
for a, b in zip(A, B):
    dp_new = np.zeros(C + 1, dtype=np.int64)
    p = (P[b] - P[a - 1]) % mod
    for c in range(C + 1):
        dp_new[c] = (dp[:c + 1] * p[c::-1] % mod).sum()
    dp = dp_new % mod
print((dp[C]))
