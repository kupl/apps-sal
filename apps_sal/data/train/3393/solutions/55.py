from math import sqrt


def sum_square_divisors(n):
    res = 0
    nn = n * n
    for i in range(1, int(sqrt(n)) + 1, n % 2 + 1):
        if n % i == 0:
            ii = i * i
            res += ii
            if ii != n:
                res += nn // ii
    return res


def list_squared(m, n):
    res = []
    for i in range(m, n + 1):
        sds = sum_square_divisors(i)
        r = int(sqrt(sds))
        if r * r == sds:
            res.append([i, sds])
    return res
