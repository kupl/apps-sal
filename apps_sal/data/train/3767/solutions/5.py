import itertools
import math
digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def dec2FactString(nb):
    result = []
    i = itertools.count(1)
    while nb:
        (nb, rem) = divmod(nb, next(i))
        result.append(digits[rem])
    return ''.join((i for i in result[::-1]))


def factString2Dec(string):
    return sum((digits.index(d) * math.factorial(i) for (d, i) in zip(string[::-1], itertools.count())))
