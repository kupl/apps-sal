MOD = 10 ** 9 + 7
fact = [1]
rfact = [1]
for i in range(1, 200500):
    fact.append(fact[-1] * i % MOD)
    rfact.append(rfact[-1] * pow(i, MOD - 2, MOD) % MOD)


def cnk(n, k):
    return fact[n] * rfact[k] * rfact[n - k] % MOD


(h, w, n) = list(map(int, input().split()))
points = []
for i in range(n):
    points.append(tuple(map(int, input().split())))
points = sorted(points)
points.append((h, w))
dp = [0 for i in range(len(points))]
for i in range(len(points)):
    dp[i] = cnk(points[i][0] + points[i][1] - 2, points[i][0] - 1)
    for j in range(i):
        if points[j][0] <= points[i][0] and points[j][1] <= points[i][1]:
            dp[i] -= dp[j] * cnk(points[i][0] + points[i][1] - points[j][0] - points[j][1], points[i][0] - points[j][0])
    dp[i] %= MOD
print(dp[-1])
