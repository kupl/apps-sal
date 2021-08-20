def multiple_of_index(arr):
    return [x for (i, x) in enumerate(arr[1:], 1) if not x % i]
