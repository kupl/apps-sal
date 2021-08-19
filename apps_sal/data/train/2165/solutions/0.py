def init_factorials(N, mod):
    f = 1
    fac = [1] * N
    for i in range(1, N):
        f *= i
        f %= mod
        fac[i] = f
    return fac


def init_inv(N, mod, fac):
    b = bin(mod - 2)[2:][-1::-1]
    ret = 1
    tmp = fac[N]
    if b[0] == '1':
        ret = fac[N]
    for bi in b[1:]:
        tmp *= tmp
        tmp %= mod
        if bi == '1':
            ret *= tmp
            ret %= mod
    inv = [1] * (N + 1)
    inv[N] = ret
    for i in range(N - 1, 0, -1):
        ret *= i + 1
        ret %= mod
        inv[i] = ret
    return inv


def f(r, c, mod, fac, inv):
    return fac[r + c] * inv[r] * inv[c] % mod


def read_data():
    (h, w, n) = list(map(int, input().split()))
    blacks = []
    for i in range(n):
        (r, c) = list(map(int, input().split()))
        blacks.append((r, c))
    return (h, w, n, blacks)


def solve(h, w, n, blacks):
    mod = 10 ** 9 + 7
    fac = init_factorials(h + w + 10, mod)
    inv = init_inv(h + w + 5, mod, fac)
    ans = fac[h + w - 2] * inv[h - 1] * inv[w - 1] % mod
    eb = [(r + c, r, c) for (r, c) in blacks]
    eb.sort()
    blacks = [(r, c) for (rc, r, c) in eb]
    g = [f(r - 1, c - 1, mod, fac, inv) for (r, c) in blacks]
    hw = h + w
    for (i, (r, c)) in enumerate(blacks):
        gi = g[i]
        rc = r + c
        ans -= gi * fac[hw - rc] * inv[h - r] * inv[w - c]
        ans %= mod
        for (j, (rj, cj)) in enumerate(blacks[i + 1:], i + 1):
            if r <= rj and c <= cj:
                g[j] -= gi * fac[rj + cj - rc] * inv[rj - r] * inv[cj - c]
                g[j] %= mod
    return ans


(h, w, n, blacks) = read_data()
print(solve(h, w, n, blacks))
