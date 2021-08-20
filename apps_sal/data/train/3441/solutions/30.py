import math


def get_average(marks):
    marks_sum = 0
    for mark in marks:
        marks_sum += mark
    average_mark = marks_sum / len(marks)
    return math.floor(average_mark)


print(get_average([2, 5, 13, 20, 16, 16, 10]))
