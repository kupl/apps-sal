def invite_more_women(arr):
    w = arr.count(1)
    m = arr.count(-1)
    if w > m:
        return True
    else:
        return False
