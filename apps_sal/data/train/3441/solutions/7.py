import math


def get_average(marks):
    sum = 0
    for num in marks:
        sum += num
    total = sum / len(marks)
    return math.floor(total)
