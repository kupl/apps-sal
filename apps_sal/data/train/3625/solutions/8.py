from itertools import groupby


def sum_of_regular_numbers(arr):
    (r, i) = (0, 0)
    for (k, g) in groupby((j - i for (i, j) in zip(arr, arr[1:]))):
        x = len(list(g))
        if x > 1:
            r += sum(arr[i:i + x + 1])
        i += x
    return r
