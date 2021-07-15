import math

def get_average(marks):
    sum = 0
    for mark in marks:
        sum = sum + mark
    return math.floor(sum/len(marks))

