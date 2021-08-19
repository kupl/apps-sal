def binomial_coefficient(n, r, mod=10 ** 9 + 7):
    if r < 0 or r > n:
        return 0
    res = 1
    div = 1
    r = min(r, n - r)
    for i in range(r):
        res = res * (n - i) % mod
        div = div * (i + 1) % mod
    return res * pow(div, mod - 2, mod) % mod


mod = 10 ** 9 + 7
(n, m) = map(int, input().split())
A = list(map(int, input().split()))
ans = binomial_coefficient(n + m, sum(A) + n, mod)
print(ans)
