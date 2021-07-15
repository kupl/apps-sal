def find_uniq(arr):
    x = arr[0 if arr[0] == arr[1] else 2]
    return next(y for y in arr if y != x)
