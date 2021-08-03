from math import sqrt


def divisors(n):
    res = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            res += 2
    if int(sqrt(n))**2 == n:
        res -= 1
    return res
