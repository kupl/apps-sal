import math


def new_avg(arr, newavg):
    a = math.ceil(newavg * (len(arr) + 1) - sum(arr))
    if a > 0:
        return(a)
    return Error
