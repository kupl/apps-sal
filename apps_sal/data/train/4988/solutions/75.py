import math

def __pow(a, b=2):
    return pow(a, b)

math.pow = __pow
square = math.pow
