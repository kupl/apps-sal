def diff(arr):
    r = arr and max(arr, key = lambda x : abs(eval(x)))
    return bool(arr and eval(r)) and r
