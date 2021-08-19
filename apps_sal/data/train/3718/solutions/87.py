import math


def divisors(n):
    cnt = 0
    for i in range(1, n + 1, 1):
        if n % i == 0:
            if n / i == i:
                cnt = cnt + 1
            else:
                cnt = cnt + 1
    return cnt
