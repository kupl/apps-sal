from math import pi
import math


def converter(n, decimals=0, base=pi):
    print(n)
    print(decimals)
    print(base)
    negative = False
    retVal = ''
    if n == 0:
        left = 0
    else:
        if n < 0:
            n = n * -1
            negative = True
            retVal = '-'
        left = math.floor(math.log(abs(n)) / math.log(base))
    charList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for p in range(left, 0 - decimals - 1, -1):
        if p == -1:
            retVal += '.'
        coeff = math.pow(base, p)
        print('XXXXXXXX')
        print(n)
        print(coeff)
        print('XXXXXXXX')
        print(math.floor(n / coeff))
        retVal += charList[math.floor(n / coeff)]
        n = n - math.floor(n / coeff) * coeff
    print(retVal)
    return retVal
