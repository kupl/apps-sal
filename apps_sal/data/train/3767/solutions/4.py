from string import digits, ascii_uppercase
from math import factorial
BASE = digits + ascii_uppercase
FACT = [factorial(a) for a in range(36, -1, -1)]


def dec2FactString(nb):
    res = []
    for fact in FACT:
        (d, nb) = divmod(nb, fact)
        res.append(BASE[d])
    return ''.join(res).lstrip('0')


def factString2Dec(string):
    return sum((BASE.index(a) * FACT[c] for (c, a) in enumerate(string, -len(string))))
