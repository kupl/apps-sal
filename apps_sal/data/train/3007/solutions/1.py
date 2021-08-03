from math import sqrt


def consecutive_sum(n):
    cnt = 0
    lim = int(sqrt(2 * n))
    m = 1
    while m <= lim:
        u = n / m + m / 2 + 0.5
        if int(u) == u:
            cnt += 1
        m += 1
    return cnt
