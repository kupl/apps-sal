def invite_more_women(arr):
    if arr.count(1) == arr.count(-1) or arr.count(-1) == len(arr):
        return False
    return True
