import numpy as np
MOD = 998244353
inv2 = pow(2, MOD - 2, MOD)

factorial = [1] * 301
for n in range(1, 301):
    factorial[n] = n * factorial[n - 1] % MOD

N, K = map(int, input().split())
A = np.array(list(map(int, input().split())))

S = [0] * (K + 1)
S[0] = N
temp = np.array([1] * N)
for x in range(1, K + 1):
    temp = temp * A % MOD
    S[x] = int(np.sum(temp))

for X in range(1, K + 1):
    ans = 0
    for x in range(X + 1):
        comb = factorial[X] * pow(factorial[x], MOD - 2, MOD) * pow(factorial[X - x], MOD - 2, MOD) % MOD
        ans += comb * S[x] * S[X - x] % MOD
    ans -= pow(2, X, MOD) * S[X] % MOD
    ans *= inv2
    ans %= MOD
    print(ans)
