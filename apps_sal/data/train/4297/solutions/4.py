def get_mean(arr, x, y):
    from numpy import mean
    if 1 < x <= len(arr) and 1 < y <= len(arr):
        return mean((mean(arr[:x]), mean(arr[-y:])))
    else:
        return -1

