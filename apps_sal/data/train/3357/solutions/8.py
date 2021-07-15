def find_dup(arr):
    return next(n for n in arr if arr.count(n) == 2)

