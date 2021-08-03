from math import log


def decompose(num):
    i, res = 2, []
    while i**2 <= num:
        n = int(log(num, i))
        res.append(n)
        num -= i**n
        i += 1
    return [res, num]
