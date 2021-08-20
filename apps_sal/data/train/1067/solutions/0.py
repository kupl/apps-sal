MOD = 1000000007


def fib(n):
    F = [[2, 2], [1, 0]]
    power(F, n - 1)
    ans = [6, 2]
    return (F[0][0] * 6 + F[0][1] * 2) % MOD


def multiply(F, M):
    x = (F[0][0] * M[0][0] + F[0][1] * M[1][0]) % MOD
    y = (F[0][0] * M[0][1] + F[0][1] * M[1][1]) % MOD
    z = (F[1][0] * M[0][0] + F[1][1] * M[1][0]) % MOD
    w = (F[1][0] * M[0][1] + F[1][1] * M[1][1]) % MOD
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, n):
    if n == 0 or n == 1:
        return
    M = [[2, 2], [1, 0]]
    power(F, n // 2)
    multiply(F, F)
    if n % 2 != 0:
        multiply(F, M)


for _ in range(int(input())):
    n = int(input())
    ans = 1
    if n == 0:
        ans = 1
    elif n == 1:
        ans = 2
    elif n == 2:
        ans = 6
    else:
        ans = fib(n - 1)
    print(ans)
