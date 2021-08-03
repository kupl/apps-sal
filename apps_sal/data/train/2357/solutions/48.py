N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
X, Y = M + N, sum(A) + N
p = 10**9 + 7


def nCr(n, r, mod=p):
    a, b = 1, 1
    for i in range(r):
        a *= n - i
        a %= mod
        b *= i + 1
        b %= mod
    return (a * pow(b, mod - 2, mod)) % mod


print((nCr(X, Y, p)))
