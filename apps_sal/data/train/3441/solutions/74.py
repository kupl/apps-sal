import statistics
import math


def get_average(marks):
    get_mean = statistics.mean(marks)
    rounded = math.floor(get_mean)
    return rounded

