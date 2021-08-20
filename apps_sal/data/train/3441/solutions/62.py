import math


def get_average(marks):
    marks_sum = 0
    for i in marks:
        marks_sum += i
    return int(marks_sum / len(marks))
