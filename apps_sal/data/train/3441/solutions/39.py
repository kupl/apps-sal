from math import *


def get_average(marks):
    result = 0
    for index in marks:
        result = result + index
    result = (result / len(marks))
    return floor(result)
