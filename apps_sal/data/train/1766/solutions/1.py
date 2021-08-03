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
    # e.g  (A) 1    -> 1
    # e.g  (B) 10   -> ( (1) * (-2) + 0 )
    # e.g  (C) 101  -> ( (1) * (-2) + 0 ) * (-2) + 1 = B * (-2) + 1
    # e.g  (D) 1010 -> C * (-2) + 0
    # ...
    return toDecimal(number[:-1]) * (-2) + int(number[-1])

# posCurrentOne is the position (0 is position of the right digit) of
# the last 1 knew (left to right)
# at the begining we don't know this position so we arbitrarily initialize
# this to -1. It is useful for insert the zerros after


def toWBinary(number, posCurrentOne=int(-1)):
    s = ''

    if not(number):
        if posCurrentOne == -1:
            return '0'
        # if we know the last 1 is in position 2, and the number is egal to 0,
        # then we can complete with 2 zerros after and return the result
        s += '0' * posCurrentOne
        return s

    # We begin by calculate the number of digit necessary
    # if number is egal to  1 we need 1 digits
    # if number is egal to  2 we need 3 digits
    # if number is egal to -1 we need 2 digits
    # ...

    # if the number is > 0, we need odd  digits
    # if the number is < 0, we need even digits

    # if number is > 0, if the number of digits usefull is N, then the greatest
    # number possible is :

    # (-2 ** 0)                         = 1 for 1 digit
    # (-2 ** 0) + (-2 ** 2)             = 5 for 3 digits
    # (-2 ** 0) + (-2 ** 2) + (-2 ** 4) = 21 for 4 digits

    # so with S the max number with N digits we have:
    # S = sum(i=1,(N+1)/2) [(-2) ** (2 * (i - 1))]
    # it is egal to
    # S = sum(i=0,(N-1)/2) [4 ** i]
    # so
    # S  = 1 + 4 + ... + 4 ** ((N-1)/2)
    # in multiply per 4
    # 4S =     4 + ... + 4 ** ((N-1)/2) + 4 ** ((N+1)/2)
    # with substraction
    # 4S - S = 4 ** ((N+1)/2) - 1
    # S = (4 ** ((N+1)/2) - 1) / 3

    # with x the decimal number to convert,
    # whe surch N so that
    # S >= x

    # 4 ** ((N+1)/2) - 1 / 3 >= x
    # 4 ** ((N+1)/2)         >= 3x + 1

    # we use the log
    # ((N+1) / 2) log(4)     >= log(3x + 1)

    # but log(4) = log(2*2) = 2log(2) so
    # (N+1) log(2)           >= log(3x + 1)
    #                      N >= (log(3x + 1) / log(2)) - 1
    #
    # and we must have N integer and odd
    # so we use ceil and if the result is even we add 1
    # we have also N the number of digit necessary. And so we know
    # the digit in position N-1 is egal to 1

    if number > 0:
        N = int(ceil(log(3 * number + 1, 2)) - 1)
        if not(N % 2):
            N += 1

    # by the same way we calculate N if number is > 0
    else:
        N = int(ceil(log((-3) * number + 2, 2)) - 1)
        if (N % 2):
            N += 1

    # if the last one calculate is in position 2 and we need 1 digit
    # we insert 2 - 1 = 1 zerro and one 1
    s += '0' * (posCurrentOne - N)
    s += '1'

    # if we have N digits, the digit in position N-1 is to one
    # and correspond to (-2) ** (N-1). So we can substract this value
    # and iterate. We indicate so the position N -1

    return s + toWBinary(number - ((-2) ** (N - 1)), N - 1)
