def shuffle_it(arr, *ars):
    for [x, y] in ars:
        arr[x], arr[y] = arr[y], arr[x]
    return arr
