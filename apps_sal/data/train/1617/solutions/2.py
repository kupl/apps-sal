from math import pi


def converter(n, decimals=0, base=pi):
    newbase = ""
    temp = base
    highdigit = 1
    if n < 0:
        newbase = "-"
        n *= -1
    while temp <= n:
        temp *= base
        highdigit += 1
    for i in reversed(list(range(-decimals, highdigit))):
        temp = int(n / (base ** i))
        if temp > 9:
            digit = chr(55 + temp)
        else:
            digit = str(temp)
        newbase += digit
        n -= temp * base ** i
        if i == 0 and decimals > 0:
            newbase += "."
    return newbase
