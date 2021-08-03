from math import ceil, floor


def round_it(n):
    arr = str(n).split(".")
    return ceil(n) if len(arr[0]) < len(arr[1]) else round(n) if len(arr[0]) == len(arr[1]) else floor(n)
