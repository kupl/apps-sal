(N, K) = list(map(int, input().split()))
Mod = 998244353
DP = [0] * (N + 1)
DP[0] = 1
for x in range(1, N + 1):
    (ODP, DP) = (DP, [0] * (N + 1))
    for k in range(N, -1, -1):
        DP[k] = ODP[k - 1]
        if 2 * k <= N:
            DP[k] += DP[2 * k]
            DP[k] %= Mod
print(DP[K])
