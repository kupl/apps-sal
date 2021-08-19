def sum_good(x):
    return sum(x) - min(x) - max(x) * bool(x[1:])


def sum_array(arr):
    return sum_good(arr or [0])
