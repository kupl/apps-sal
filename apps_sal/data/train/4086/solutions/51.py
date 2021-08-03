def first_non_consecutive(arr):
    return next((i for i in arr if not min(arr) + arr.index(i) == i), None)
