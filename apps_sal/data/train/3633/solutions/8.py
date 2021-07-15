def shuffle_it(*args):
    arr, *args = args
    for i1, i2 in args:
        arr[i1], arr[i2] = arr[i2], arr[i1]
    return arr
