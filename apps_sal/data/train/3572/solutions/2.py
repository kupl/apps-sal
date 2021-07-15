def invite_more_women(arr):
    x = arr.count(-1)
    y = arr.count(1)
    if x >= y:
        return 0
    else:
        return 1
