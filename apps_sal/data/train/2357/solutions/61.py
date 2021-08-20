mod = 10 ** 9 + 7


def comb(n, m):
    ans = 1
    (a, b) = (1, 1)
    for i in range(1, m + 1):
        a = a * (n - i + 1) % mod
        b = b * i % mod
        ans %= mod
    return a * pow(b, mod - 2, mod) % mod


(N, M) = map(int, input().split())
S = sum(map(int, input().split()))
print(comb(M + N, S + N))
