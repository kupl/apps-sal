import math


def get_average(marks):
    sum = 0
    for n in marks:
        sum += n
    length = len(marks)
    average = sum / length
    return math.floor(average)
