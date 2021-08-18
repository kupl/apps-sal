import sys

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
P = int(1e9 + 7)
sumA = sum(A)


def comb(n, r):
    if n < r or r < 0:
        return 0
    nume = 1
    deno = 1
    for i in range(1, r + 1):
        nume = (nume * (n - i + 1)) % P
        deno = (deno * i) % P
    deno_inv = pow(deno, P - 2, P)
    return nume * deno_inv % P


print((comb(M + N, N + sumA)))
