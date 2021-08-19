def invite_more_women(arr):
    x = arr.count(-1)
    n = arr.count(1)
    if x < n:
        return True
    return False
