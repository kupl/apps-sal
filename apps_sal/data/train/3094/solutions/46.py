def sum_array(arr):
    if arr is None:
        return 0
    elif len(arr) <= 1:
        return 0
    a = max(arr)
    b = min(arr)
    c = sum(arr)
    return c - a - b
