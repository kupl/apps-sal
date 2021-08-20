def v(k, n):
    return 1 / (k * (n + 1) ** (2 * k))


def u(k, N):
    u_res = 0
    for n in range(0, N):
        u_res += v(k, n + 1)
    return u_res


def S(K, N):
    S_res = 0
    for k in range(0, K):
        S_res += u(k + 1, N)
    return S_res


def doubles(maxk, maxn):
    return S(maxk, maxn)
