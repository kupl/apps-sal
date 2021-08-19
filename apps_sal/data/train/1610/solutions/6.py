import math


def f1(n):
    (x, s) = (1, 0)
    while 2 ** x <= n:
        s = s + math.floor(n / 2 ** x)
        x = x + 1
    return s


def subsets_parity(n, k):
    if n == k:
        return 'ODD'
    if n > 0 and k > 0 and (n - k > 0):
        if f1(n) == f1(k) + f1(n - k):
            return 'ODD'
        else:
            return 'EVEN'
