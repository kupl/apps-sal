def first_non_consecutive(arr):
    for i, q in enumerate(arr, arr[0]):
        if i != q:
            return q
