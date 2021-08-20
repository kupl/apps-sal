import math


def is_divide_by(number, a, b):
    div = abs(number % a)
    div2 = abs(number % b)
    correto = False
    if div == 0 and div2 == 0:
        correto = True
    return correto
