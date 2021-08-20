def first_non_consecutive(arr):
    return next((y for (x, y) in zip(arr, arr[1:]) if y - x > 1), None)
