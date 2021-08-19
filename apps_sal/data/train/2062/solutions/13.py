import sys
SIZE = 5 * 10 ** 3
MOD = 10 ** 9 + 7
SIZE += 1
inv = [0] * SIZE
fac = [0] * SIZE
finv = [0] * SIZE
fac[0] = fac[1] = 1
finv[0] = finv[1] = 1
for i in range(2, SIZE):
    fac[i] = fac[i - 1] * i % MOD
finv[-1] = pow(fac[-1], MOD - 2, MOD)
for i in range(SIZE - 1, 0, -1):
    finv[i - 1] = finv[i] * i % MOD
    inv[i] = finv[i] * fac[i - 1] % MOD


def choose(n, r):
    if 0 <= r <= n:
        return fac[n] * finv[r] % MOD * finv[n - r] % MOD
    else:
        return 0


def chofuku(ball, box):
    return choose(box + ball - 1, box)


read = sys.stdin.read
readline = sys.stdin.readline
(n, a, b, c, d) = list(map(int, read().split()))
dp = [0] * (n + 1)
dp[0] = 1
for i in range(a, b + 1):
    invmod = [1]
    for p in range(1001 // i + 2):
        invmod.append(invmod[-1] * finv[i] % MOD)
    coeff = [fac[i * p] * invmod[p] % MOD * finv[p] % MOD for p in range(1001 // i + 2)]
    ndp = dp[:]
    for j in range(n + 1):
        for p in range(c, d + 1):
            if j + i * p > n:
                break
            ndp[j + i * p] += coeff[p] * dp[j] % MOD * choose(n - j, i * p)
            ndp[j + i * p] %= MOD
    dp = ndp
print(dp[n] % MOD)
