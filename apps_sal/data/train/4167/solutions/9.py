def descriptions(arr):
    return 2 ** sum((x + 1 == y for (x, y) in zip(arr, arr[1:])))
