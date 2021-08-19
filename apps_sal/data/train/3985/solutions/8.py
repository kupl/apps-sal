def find_even_index(arr):
    return next((i for (i, __) in enumerate(arr) if sum(arr[:i]) == sum(arr[i + 1:])), -1)
