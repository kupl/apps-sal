def mod_combination(n, k, mod = 10 ** 9 + 7):
    def extended_gcd(a, b):
        if b == 0:
            return (a, 1, 0)
        d, x, y = extended_gcd(b, a % b)
        return (d, y, x - (a // b) * y)
    p, q = 1, 1
    for i in range(n - k + 1, n + 1):
        p = (p * i) % mod
    for i in range(2, k + 1):
        q = (q * i) % mod
    return p * (extended_gcd(q, mod)[1] % mod) % mod


N, M, *A = map(int, open(0).read().split())

S = sum(A)
print(mod_combination(M + N, S + N))
