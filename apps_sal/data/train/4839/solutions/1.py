def new_avg(arr, newavg):
    extra = newavg * float(len(arr) + 1) - sum(arr)
    if extra < 0:
        raise ValueError
    return int(extra + 0.999)
