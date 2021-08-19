import sys
readline = sys.stdin.readline
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    import numpy as np

    def combmoddp():
        n = 400
        comb = np.array([[0] * (n + 1) for _ in range(n + 1)])
        comb[0][0] = 1
        for i in range(1, n + 1):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD
        return comb
    MOD = 998244353
    (N, K) = list(map(int, readline().split()))
    A = np.array(list(map(int, readline().split())), np.int64)
    s = np.array([0] * (K + 1), np.int64)
    t = np.array([1] * N, np.int64)
    for i in range(K + 1):
        s[i] = np.sum(t) % MOD
        t = t * A
        t = np.remainder(t, MOD)
    comb = combmoddp()
    d = np.array([1] * N, np.int64)
    inv2 = pow(2, MOD - 2, MOD)
    for x in range(1, K + 1):
        ans = 0
        for i in range(x + 1):
            t = s[i] * s[x - i] % MOD
            t = t * comb[x][i] % MOD
            ans += t
        ans %= MOD
        d = 2 * A * d
        d = np.remainder(d, MOD)
        ans -= np.sum(d)
        ans %= MOD
        ans *= inv2
        ans %= MOD
        print(ans)


def __starting_point():
    main()


__starting_point()
