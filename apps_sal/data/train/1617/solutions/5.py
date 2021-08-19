from math import pi, log, floor


def converter(n, decimals=0, base=pi):
    if n < 0:
        isNegative = True
        n *= -1
    else:
        isNegative = False
    if n == 0:
        digits = 1
    else:
        digits = floor(log(n) / log(base) + 1)
    piggyBank = n
    base36 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}
    output = ''
    power = digits - 1
    debugList = []
    while power >= 0:
        newDig = floor(piggyBank / base ** power)
        piggyBank -= newDig * base ** power
        if newDig >= 10:
            newDig = base36[newDig]
        output += str(newDig)
        power -= 1
    if decimals > 0:
        output += '.'
    while power * -1 <= decimals:
        newDig = floor(piggyBank / base ** power)
        piggyBank -= newDig * base ** power
        if newDig >= 10:
            newDig = base36[newDig]
        output += str(newDig)
        power -= 1
    if isNegative:
        output = '-' + output
    return output
