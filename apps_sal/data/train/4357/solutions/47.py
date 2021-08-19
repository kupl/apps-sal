def nth_smallest(arr, pos):
    if len(arr) < 3:
        return 'Array needs to be longer'
    a = sorted(arr)
    real_index = pos - 1
    b = a[real_index]
    return b
