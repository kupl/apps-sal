def new_avg(arr, newavg):
    value = round(len(arr) * newavg - (sum(arr) - newavg) + 0.49)
    if value < 0:
        raise ValueError('Error expected')
    return value
