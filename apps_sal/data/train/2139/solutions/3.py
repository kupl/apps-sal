import sys
readline = sys.stdin.readline
MOD = 998244353


def make_fac(limit):
    fac = [1] * limit
    for i in range(2, limit):
        fac[i] = i * fac[i - 1] % MOD
    faci = [0] * limit
    faci[-1] = pow(fac[-1], MOD - 2, MOD)
    for i in range(limit - 2, 0, -1):
        faci[i] = faci[i + 1] * (i + 1) % MOD
    return (fac, faci)


(fac, faci) = make_fac(341398)


def comb(a, b):
    if not a >= b >= 0:
        return 0
    return fac[a] * faci[b] * faci[a - b] % MOD


N = int(readline())
A = list(map(int, readline().split()))
A.sort()
print((sum(A[N:]) - sum(A[:N])) % MOD * comb(2 * N, N) % MOD)
