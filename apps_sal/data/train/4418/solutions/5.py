def get_function(arr):
    if len(set((j - i for (i, j) in zip(arr, arr[1:])))) != 1:
        return 'Non-linear sequence'
    else:
        return lambda x: arr[0] + (arr[2] - arr[1]) * x
