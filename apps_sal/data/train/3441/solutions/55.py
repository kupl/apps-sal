import math


def get_average(marks):
    count = 0
    average = 0
    for num in marks:
        count += num
    average = count / len(marks)
    return math.floor(average)
