fact = [1]
fTQJsiXxvUFMlBVGazWH = int
fTQJsiXxvUFMlBVGazWp = map
fTQJsiXxvUFMlBVGazWC = input
fTQJsiXxvUFMlBVGazWn = range
fTQJsiXxvUFMlBVGazWg = max
fTQJsiXxvUFMlBVGazWo = pow
fTQJsiXxvUFMlBVGazWu = tuple
fTQJsiXxvUFMlBVGazWI = print
rfact = [1]
MOD = fTQJsiXxvUFMlBVGazWH(1000000000.0) + 7
(n, m, k) = fTQJsiXxvUFMlBVGazWp(fTQJsiXxvUFMlBVGazWH, fTQJsiXxvUFMlBVGazWC().split())
for i in fTQJsiXxvUFMlBVGazWn(1, fTQJsiXxvUFMlBVGazWg(2 * n, 2 * m) + 2):
    fact += [fact[-1] * i % MOD]
    rfact += [rfact[-1] * fTQJsiXxvUFMlBVGazWo(i, MOD - 2, MOD) % MOD]


def cmb(n, k):
    return fact[n] * rfact[k] * rfact[n - k] % MOD


points = [fTQJsiXxvUFMlBVGazWu(fTQJsiXxvUFMlBVGazWp(fTQJsiXxvUFMlBVGazWH, fTQJsiXxvUFMlBVGazWC().split())) for i in fTQJsiXxvUFMlBVGazWn(k)]
points += [(n, m)]
points.sort()
dp = []
for i in fTQJsiXxvUFMlBVGazWn(k + 1):
    tmp = cmb(points[i][0] + points[i][1] - 2, points[i][0] - 1)
    for j in fTQJsiXxvUFMlBVGazWn(i):
        if points[j][0] <= points[i][0] and points[j][1] <= points[i][1]:
            tmp -= dp[j] * cmb(points[i][0] - points[j][0] + points[i][1] - points[j][1], points[i][1] - points[j][1]) % MOD
            tmp += MOD
            tmp %= MOD
    dp += [tmp]
fTQJsiXxvUFMlBVGazWI(dp[k])
