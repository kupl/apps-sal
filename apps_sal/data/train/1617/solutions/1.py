from math import pi
from math import log

def converter(n, decimals=0, base=pi):
    DIGITS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    representation = []
    if (n < 0):
        representation.append('-')
        n *= -1
    if (n == 0):
        decimalCount = 0
    else: 
        decimalCount = int(log(n, base))
    for dplace in [pow(base, power) for power in range(decimalCount, -1 - decimals, -1)]:
        rNumber = int(n / dplace)
        n -= rNumber * dplace
        representation.append(DIGITS[rNumber])
        if dplace == 1 and decimals > 0: 
            representation.append('.')
    return ''.join(representation)

