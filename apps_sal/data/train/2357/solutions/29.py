(N, M) = map(int, input().split())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7


def binomial_coefficients(n, k):
    numera = 1
    denomi = 1
    for i in range(k):
        numera *= n - i
        numera %= mod
        denomi *= i + 1
        denomi %= mod
    return numera * pow(denomi, -1, mod) % mod


print(binomial_coefficients(M + N, N + sum(A)))
