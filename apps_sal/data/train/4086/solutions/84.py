def first_non_consecutive(arr):
    for i, v in enumerate(arr, arr[0]):
        if i != v:
            return i + 1
    return None
