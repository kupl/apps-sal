def descriptions(arr):
    return 2**len([v for n, v in enumerate(arr) if v == arr[n - 1] + 1])
