import math
def get_average(marks):
    x = 0
    y = 0
    for mark in marks:
        x = x + 1
        y = y + mark
    return math.floor(y / x)
