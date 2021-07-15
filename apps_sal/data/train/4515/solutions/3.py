def diff(arr):
    if not arr: return 0
    m = max(arr, key=lambda x: abs(eval(x)))
    return eval(m) and m
