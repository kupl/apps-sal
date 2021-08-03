import numpy as np
MOD = 1000000007

N, K = list(map(int, input().split()))
a = np.ones(N)

for i in range(K - 1):
    a = np.cumsum(a)
    a = np.mod(a, MOD)
print(int(np.sum(a)) % MOD)
