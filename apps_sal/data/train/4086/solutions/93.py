def first_non_consecutive(arr):
    return next((arr[i] for i in range(1, len(arr)) if arr[i] - 1 != arr[i - 1]), None)
