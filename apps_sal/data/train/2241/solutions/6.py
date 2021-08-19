MOD = 10 ** 9 + 7
tab = []
for i in range(401):
    now = []
    cnt = 0
    for q in range(401):
        cnt += pow(q, i, MOD)
        now.append(cnt)
    tab.append(now[:])
(n, c) = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
enji = []
for i in range(n):
    now = []
    for q in range(c + 1):
        now.append(tab[q][B[i]] - tab[q][A[i] - 1])
    enji.append(now[:])
dp = [0 for i in range(c + 1)]
dp[0] = 1
ndp = [0 for i in range(c + 1)]
for i in range(n):
    for step in range(c + 1):
        val = enji[i][step] % MOD
        for fr in range(c + 1 - step):
            ndp[fr + step] += dp[fr] * val % MOD
            ndp[fr + step] %= MOD
    dp = ndp[:]
    ndp = [0 for i in range(c + 1)]
print(dp[-1])
