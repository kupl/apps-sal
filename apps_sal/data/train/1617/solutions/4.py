from math import pi
import math

numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def converter(n, decimals=0, base=pi):
    if n < 0:
        return '-' + converter(-n, decimals, base)
    result = ''
    digits = 0
    while n >= base ** digits:
        digits += 1

    for i in range(digits - 1, -decimals - 1, -1):
        div = n / (base ** i)
        integer = math.floor(div)
        n = n - integer * (base ** i)
        result = result + numbers[int(integer)]

    if decimals > 0:
        result = result[:-decimals] + '.' + result[-decimals:]
    if result[0] == '.':
        result = '0' + result
    return result
