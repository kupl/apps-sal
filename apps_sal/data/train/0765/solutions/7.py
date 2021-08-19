from math import *


def karatsuba(x, y):
    tmp = 10
    if x < 10 or y < 10:
        return x * y
    m = max(int(log10(x) + 1), int(log10(y) + 1))
    if m % 2 != 0:
        m -= 1
    m_2 = int(m / 2)
    (a, b) = divmod(x, tmp ** m_2)
    (c, d) = divmod(y, tmp ** m_2)
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd
    return ac * 10 ** m + bd + ad_bc * 10 ** m_2


def solve(array, r):
    i = 0
    res = 1
    while i * r < len(array):
        res = karatsuba(res, array[i * r])
        i += 1
    return ' '.join((str(res)[0], str(res % (10 ** 9 + 7))))


def frjump():
    N = int(input())
    friendliness = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            friendliness[query[1] - 1] = query[2]
        else:
            (types, R) = query
            print(solve(friendliness, R))


def __starting_point():
    frjump()


__starting_point()
