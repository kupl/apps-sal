import re


def withdraw(n):
    return [len(a) // b for (a, b) in zip(re.findall('\\A((?:.{10})*)((?:.{5})*)((?:.{2})*)\\Z', '.' * (n // 10))[0], (10, 5, 2))]
