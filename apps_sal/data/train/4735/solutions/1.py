from bisect import bisect_left


def keep_order(arr, val):
    return bisect_left(arr, val)
