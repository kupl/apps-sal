from math import floor
def get_average(marks):
    sum = 0
    for mark in marks:
        sum += mark
    return floor(sum / len(marks))
        

