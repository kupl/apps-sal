def peak(arr):
    for (i, val) in enumerate(arr):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1
