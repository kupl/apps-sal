def binary(x):
    result = []
    while True:
        remainder = x % 2
        result.append(str(remainder))
        x = x // 2

        if x == 0:
            break

    result.reverse()
    return "".join(result)

def octal(x):
    result = []
    while True:
        remainder = x % 8
        result.append(str(remainder))
        x = x // 8

        if x == 0:
            break

    result.reverse()
    return "".join(result)

def hexadecimal(x):
    result = []
    while True:
        remainder = x % 16

        if remainder == 10:
            result.append('a')
        elif remainder == 11:
            result.append('b')
        elif remainder == 12:
            result.append('c')
        elif remainder == 13:
            result.append('d')
        elif remainder == 14:
            result.append('e')
        elif remainder == 15:
            result.append('f')
        else:
            result.append(str(remainder))

        x = x // 16
        if x == 0:
            break

    result.reverse()
    return "".join(result)

import math

def func(l):
    average = math.floor(sum(l) / len(l))
    result = [average, binary(average), octal(average), hexadecimal(average)]
    return result
