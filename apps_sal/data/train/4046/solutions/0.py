from math import ceil


def calculate_scrap(arr, n):
    x = 50
    for i in arr:
        x /= (1 - i / 100)
    return ceil(n * x)
