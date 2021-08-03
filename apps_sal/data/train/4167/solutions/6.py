def descriptions(arr):
    return 2**sum(j - i == 1 for i, j in zip(arr, arr[1:]))
