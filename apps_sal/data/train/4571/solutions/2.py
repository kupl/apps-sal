from math import log


def decompose(num):
    res = []
    i = 2
    while i * i <= num:
        k = int(log(num, i))
        res.append(k)
        num -= i ** k
        i += 1
    return [res, num]
