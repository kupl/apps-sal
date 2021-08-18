from math import log
from math import ceil


def skrzat(base, number):

    if base == 'b':
        return 'From binary: ' + number + ' is ' + str(toDecimal(number))

    if base == 'd':
        return 'From decimal: ' + str(number) + ' is ' + toWBinary(number)


def toDecimal(number):
    if len(number) == 1:
        return int(number)
    return toDecimal(number[:-1]) * (-2) + int(number[-1])


def toWBinary(number, posCurrentOne=int(-1)):
    s = ''

    if not(number):
        if posCurrentOne == -1:
            return '0'
        s += '0' * posCurrentOne
        return s

    if number > 0:
        N = int(ceil(log(3 * number + 1, 2)) - 1)
        if not(N % 2):
            N += 1

    else:
        N = int(ceil(log((-3) * number + 2, 2)) - 1)
        if (N % 2):
            N += 1

    s += '0' * (posCurrentOne - N)
    s += '1'

    return s + toWBinary(number - ((-2) ** (N - 1)), N - 1)
