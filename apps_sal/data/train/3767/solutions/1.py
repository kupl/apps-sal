from math import factorial
from itertools import dropwhile
DIGITS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
BASIS = [factorial(n) for n in range(len(DIGITS))]


def dec2FactString(nb):
    representation = []
    for b in reversed(BASIS):
        representation.append(DIGITS[nb // b])
        nb %= b
    return ''.join(dropwhile(lambda x: x == '0', representation))


def factString2Dec(string):
    return sum((BASIS[i] * DIGITS.index(d) for (i, d) in enumerate(reversed(string))))
