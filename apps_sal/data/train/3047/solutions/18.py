from itertools import groupby


def repeating_fractions(a, b):
    arr, idx = ["".join(grp) for num, grp in groupby(str(a / b))], 2
    while idx < len(arr):
        if len(arr[idx]) > 1:
            arr[idx] = f"({arr[idx][0]})"
        idx += 1
    return ''.join(arr)
