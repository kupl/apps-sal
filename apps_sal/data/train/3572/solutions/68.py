def invite_more_women(arr):
    if 2 <= len(arr) <= 50:
        if arr.count(-1) < arr.count(1):
            return True
        else:
            return False

    else:
        return False
