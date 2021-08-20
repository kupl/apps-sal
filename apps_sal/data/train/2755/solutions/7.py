def multiple_of_index(arr):
    return [x for (y, x) in enumerate(arr[1:], 1) if not abs(x) % y]
