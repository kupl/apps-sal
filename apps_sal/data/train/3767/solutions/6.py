import math
DIGITS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_digit(digit):
    return DIGITS[digit]


def dec2FactString(nb, f=0):
    if f == 0:
        return dec2FactString(nb, 1) + '0'
    elif nb == 0:
        return ''
    else:
        fact = math.factorial(f)
        digit = nb // fact % (f + 1)
        return dec2FactString(nb - digit * fact, f + 1) + get_digit(digit)


def factString2Dec(string):
    return sum((DIGITS.index(string[-(k + 1)]) * math.factorial(k) for k in range(0, len(string))))
