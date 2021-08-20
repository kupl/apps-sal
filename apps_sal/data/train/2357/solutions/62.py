(N, M) = map(int, input().split())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
S = sum(A)


def cmb(a, b, mod):
    if a < b:
        return 0
    b = min(b, a - b)
    num = 1
    for i in range(b):
        num = num * (a - i) % mod
    den = 1
    for i in range(1, b + 1):
        den = den * i % mod
    return num * pow(den, mod - 2, mod) % mod


print(cmb(M + N, S + N, mod))
