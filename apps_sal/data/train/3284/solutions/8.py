import math

def two_decimal_places(number):
    if number >= 0:
        return math.floor(number * 100)/100
    else:
        return math.ceil(number * 100)/100
