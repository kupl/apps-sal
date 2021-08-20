def first_non_consecutive(arr):
    return next((j for (i, j) in zip(arr, arr[1:]) if i + 1 != j), None)
