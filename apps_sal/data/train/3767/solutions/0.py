from math import factorial
from string import digits, ascii_uppercase
DIGITS = digits + ascii_uppercase
FACTORIALS = [1, 1]
f = 1
for i in range(2, 36):
    f *= i
    FACTORIALS.append(f)


def dec2FactString(nb):
    ret = []
    for f in reversed(FACTORIALS):
        (d, nb) = divmod(nb, f)
        if d or ret:
            ret.append(DIGITS[d])
    return ''.join(ret)


def factString2Dec(string):
    return sum((DIGITS.index(d) * f for (d, f) in zip(reversed(string), FACTORIALS)))
