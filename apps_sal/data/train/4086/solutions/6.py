def first_non_consecutive(arr):
    for (i, j) in zip(arr, arr[1:]):
        if abs(j - i) > 1:
            return j
    return None
