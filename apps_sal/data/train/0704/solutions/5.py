import math


def no(n):
    c = 0
    while n > 0:
        c += 1
        n //= 10
    return c


def modInverse(a, m):
    m0 = m
    y = 0
    x = 1

    if (m == 1):
        return 0

    while (a > 1):

        q = a // m

        t = m

        m = a % m
        a = t
        t = y

        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0

    return x


for _ in range(int(input())):
    a, n, m = map(int, input().split(' '))
    s = len(str(a))
    c = 10**s - 1
    w = c * m
    b = pow(10, n * s, w) - 1
    d = b // c
    ans = (d % m) * (a % m)
    print(ans % m)
