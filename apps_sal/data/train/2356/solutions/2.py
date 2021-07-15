n, k = list(map(int, input().split()))
MOD = 998244353

dp = [1]
for i in range(1, n + 1):
    ndp = [0] * (i + 1)

    for j in range(i, 0, -1):
        tmp = dp[j - 1]
        if j * 2 <= i:
            tmp += ndp[j * 2]
        ndp[j] = tmp % MOD

    dp = ndp

print((dp[k]))

