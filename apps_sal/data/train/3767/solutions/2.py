base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def fact(n):
    return fact(n - 1) * n if n else 1


def dec2FactString(nb, i=1):
    return dec2FactString(nb // i, i + 1) + base[nb % i] if nb else ''


def factString2Dec(string):
    return fact(len(string) - 1) * base.index(string[0]) + factString2Dec(string[1:]) if len(string) else 0
