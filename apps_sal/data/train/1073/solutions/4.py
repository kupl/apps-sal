def multiply(F, M, i):
    x = (F[0][0] * M[0][0] + F[1][0] * M[0][1]) % i
    y = (F[0][0] * M[1][0] + F[1][0] * M[1][1]) % i
    z = (F[0][1] * M[0][0] + F[1][1] * M[0][1]) % i
    w = (F[0][1] * M[1][0] + F[1][1] * M[1][1]) % i
    F[0][0] = x
    F[1][0] = y
    F[0][1] = z
    F[1][1] = w


def power(F, M, n, i):
    if n < 2:
        return
    power(F, M, n // 2, i)
    multiply(F, F, i)
    if n % 2 != 0:
        multiply(F, M, i)


for t in range(0, int(input())):
    i = 1000000007
    (n, m) = map(int, input().split())
    F = [[(m - 1) % i, 1], [(m - 1) % i, 0]]
    M = [[(m - 1) % i, 1], [(m - 1) % i, 0]]
    if n == 1:
        i = m % i
    elif n == 2:
        i = m * m % i
    else:
        power(F, M, n - 2, i)
        i = (F[0][0] * m + F[1][0]) * m % i
    print(i)
