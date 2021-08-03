import math


def get_average(marks):
   # raise NotImplementedError("TODO: get_average")
    marks_sum = 0
    for i in marks:
        marks_sum += i
    return int(marks_sum / len(marks))
