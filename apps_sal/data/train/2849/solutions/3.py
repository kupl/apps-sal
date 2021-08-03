def peak(arr):
    for i, n in enumerate(arr):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    else:
        return -1
