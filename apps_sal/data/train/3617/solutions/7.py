def is_zero_balanced(arr):
    return bool(arr) and sum(arr) == 0 and all((-x in arr for x in arr if x > 0))
