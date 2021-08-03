fact = [1]
rfact = [1]

MOD = int(1e9) + 7

n, m, k = list(map(int, input().split()))
for i in range(1, max(2 * n, 2 * m) + 2):
    fact += [fact[-1] * i % MOD]
    rfact += [rfact[-1] * pow(i, MOD - 2, MOD) % MOD]


def cmb(n, k):
    return fact[n] * rfact[k] * rfact[n - k] % MOD


points = [tuple(map(int, input().split())) for i in range(k)]
points += [(n, m)]

points.sort()

dp = []

for i in range(k + 1):
    tmp = cmb(points[i][0] + points[i][1] - 2, points[i][0] - 1)
    for j in range(i):
        if points[j][0] <= points[i][0] and points[j][1] <= points[i][1]:
            tmp -= (dp[j] * cmb(points[i][0] - points[j][0] + points[i][1] - points[j][1], points[i][1] - points[j][1])) % MOD
            tmp += MOD
            tmp %= MOD
    dp += [tmp]

print(dp[k])
