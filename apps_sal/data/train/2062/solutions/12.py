import numpy as np
import sys
input = sys.stdin.readline
(N, A, B, C, D) = map(int, input().split())
MOD = 10 ** 9 + 7
fact = [1] * (N + 1)
fact_inv = [1] * (N + 1)
for n in range(1, N + 1):
    fact[n] = fact[n - 1] * n % MOD
fact_inv[N] = pow(fact[N], MOD - 2, MOD)
for n in range(N, 0, -1):
    fact_inv[n - 1] = fact_inv[n] * n % MOD
fact = np.array(fact, dtype=np.int64)
fact_inv = np.array(fact_inv, dtype=np.int64)
comb = np.zeros((N + 1, N + 1), dtype=np.int64)
comb[:, 0] = 1
for n in range(1, N + 1):
    comb[n, 1:] = (comb[n - 1, 1:] + comb[n - 1, :-1]) % MOD
dp = np.zeros(N + 1, dtype=np.int64)
dp[0] = 1
for x in range(A, B + 1):
    prev = dp
    dp = prev.copy()
    for n in range(C, D + 1):
        y = n * x
        if y > N:
            break
        coef = fact[y] * pow(int(fact_inv[x]), n, MOD) % MOD * fact_inv[n] % MOD
        dp[y:] += prev[:-y] * comb[N:y - 1:-1, y] % MOD * coef
        dp %= MOD
answer = dp[N]
print(answer)
