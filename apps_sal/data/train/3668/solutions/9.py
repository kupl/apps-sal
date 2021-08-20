d = []


def s1(n):
    return 1 + 2 ** n + 3 ** n


def s2(n):
    return 1 + 2 ** n + 4 ** n


def s3(n):
    return sum((i ** n for i in range(1, 7)))


def st(n):
    return s3(n) - s2(n) - s1(n)


for i in range(1500):
    r = (st(i + 1) - 5 * st(i) - 4) // 4
    if not r % 10:
        d.append(r)


def find_mult10_SF(n):
    return d[n - 1]
