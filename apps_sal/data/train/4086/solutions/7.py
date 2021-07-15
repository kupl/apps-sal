def first_non_consecutive(arr):
    init = arr[0]
    for i in arr:
        if init != i:
            return i
        else:
            init += 1
    return None
