def is_zero_balanced(arr):
    return arr != [] and sum(arr) == 0 and all(-x in arr for x in arr)
