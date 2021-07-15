def multiple_of_index(arr):
    return [k for i, k in enumerate(arr[1:]) if not k % (i + 1)]
