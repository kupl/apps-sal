import math


def largest_power(n):
    if n == 1:
        return 0, -1
    if n <= 4:
        return 1, -1

    before = None

    r = []
    for i in range(n - 1, 1, -1):
        res = check(i)
        if res:
            return i, res


def check(n):
    c = 0
    for st in range(2, 9):
        el = round(n**(1 / st), 7)
        is_c = str(el).split('.')[1] == '0'
        if is_c:
            print(el, st, n)
            c += 1
    return c
