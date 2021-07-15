def shuffle_it(arr, *shifts):
    for (a,b) in shifts:
        arr[a], arr[b] = (arr[b], arr[a])
    return arr
