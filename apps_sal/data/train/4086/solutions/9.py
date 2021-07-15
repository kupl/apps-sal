def first_non_consecutive(arr):
    if not arr:
        return None

    for i, x in enumerate(arr, arr[0]):
        if i != x:
            return x

    return None
