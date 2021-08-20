def first_non_consecutive(arr):
    for (i, x) in enumerate(arr):
        if x != arr[i - 1] + 1 and i > 0:
            return x
    return None
