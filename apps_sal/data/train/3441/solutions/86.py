import math


def get_average(marks):
    sum = 0
    for x in marks:
        sum = sum + x
    return math.floor(sum / len(marks))
