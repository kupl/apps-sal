import sys
from sys import stdin


def modfac(n, MOD):
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    return (factorials, invs)


def modnCr(n, r, mod, fac, inv):
    return fac[n] * inv[n - r] * inv[r] % mod


mod = 998244353
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
a.sort()
(fac, inv) = modfac(2 * n + 10, mod)
print(modnCr(2 * n, n, mod, fac, inv) * (sum(a[n:]) - sum(a[:n])) % mod)
