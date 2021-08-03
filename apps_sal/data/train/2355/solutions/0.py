
import numpy as np
N, K = list(map(int, input().split()))
A = np.array(list(map(int, input().split())))
mod = 998244353

fact = [1] * (K + 1)
for i in range(1, K + 1):
    fact[i] = i * fact[i - 1] % mod
inv_fact = [pow(f, mod - 2, mod) for f in fact]

# r = [sum(pow(aa,t,mod) for aa in A)%mod for t in range(K+1)]##遅い
r = [0] * (K + 1)
r[0] = N
temp = np.ones(N, dtype="int32")
for i in range(1, K + 1):
    temp = temp * A % mod
    r[i] = int(np.sum(temp)) % mod

inv2 = pow(2, mod - 2, mod)
for x in range(1, K + 1):
    ans = sum((fact[x] * inv_fact[t] * inv_fact[x - t] * r[x - t] * r[t]) % mod
              for t in range(x + 1)) % mod
    ans -= r[x] * pow(2, x, mod) % mod
    print(((ans * inv2) % mod))
