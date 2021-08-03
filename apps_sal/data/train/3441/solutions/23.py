import math


def get_average(marks):
    t = sum(marks) / len(marks)
    return math.floor(t)
