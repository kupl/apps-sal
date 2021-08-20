def first_non_consecutive(arr):
    return next(iter((a for (a, b) in zip(arr, range(arr[0], arr[-1])) if a != b)), None)
