import math


def get_average(marks):
    sum = 0
    for i in marks:
        sum += i
    average = math.floor(sum / len(marks))
    return average
