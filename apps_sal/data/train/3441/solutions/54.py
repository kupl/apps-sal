import math


def get_average(marks):
    s = 0
    avg = 0
    for i in marks:
        s += i
        avg = s / len(marks)
    return math.floor(avg)
