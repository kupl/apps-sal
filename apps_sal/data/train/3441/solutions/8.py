import math


def get_average(marks):

    x = (len(marks))
    y = (sum(marks))

    i = y / x

    return math.floor(i)
