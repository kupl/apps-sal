from math import ceil


def new_avg(arr, newavg):
    value = int(ceil((len(arr)+1) * newavg - sum(arr)))
    if value < 0:
        raise ValueError
    
    return value
