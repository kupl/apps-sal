import math


def sum_average(arr):
    x = 0
    for i in range(0, len(arr)):
        l = len(arr[i])
        s = sum(arr[i])
        v = s / l
        x += v
    w = math.floor(x)
    return w
