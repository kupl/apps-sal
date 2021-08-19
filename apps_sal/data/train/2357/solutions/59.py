N, M = map(int, input().split())
A = list(map(int, input().split()))
mod = 10**9 + 7


def binomial_coefficients(n, k):
    numera = 1  # 分子
    denomi = 1  # 分母

    for i in range(k):
        numera *= n - i
        numera %= mod
        denomi *= i + 1
        denomi %= mod
    return numera * pow(denomi, mod - 2, mod) % mod


print(binomial_coefficients(M + N, N + sum(A)))
