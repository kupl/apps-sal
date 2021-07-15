from math import *
def new_avg(arr, newavg):
    v = ceil(newavg*(len(arr)+1) - sum(arr))
    if v >= 0:
        return v
    else:
        raise ValueError

