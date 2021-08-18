mod = 10**9 + 7
MAX = 10**3 + 100

g1 = [1, 1]
g2 = [1, 1]
for i in range(2, MAX + 1):
    num_1 = g1[-1] * i % mod
    g1.append(num_1)
    g2.append(pow(num_1, mod - 2, mod))


def cmb(n, r, MOD):
    return g1[n] * g2[r] * g2[n - r] % MOD


N, A, B, C, D = list(map(int, input().split()))

data = [[] for i in range(B + 1)]
for i in range(A, B + 1):
    for j in range(C, D + 1):
        if i * j > N:
            break
        data[i].append([i * j, pow(g2[i], j, mod) * g2[j] % mod])

dp = [0] * (N + 1)
dp[0] = 1
for i in range(A, B + 1):
    H = dp[:]
    for u, v in data[i]:
        for j in range(u, N + 1):
            H[j] = (H[j] + dp[j - u] * v) % mod
    dp = H
print((dp[N] * g1[N] % mod))
