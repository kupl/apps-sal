def sum_array(arr):
    if arr == [] or arr is None:
        return 0
    elif len(arr) == 1:
        return 0
    else:
        return sum(arr) - min(arr) - max(arr)
