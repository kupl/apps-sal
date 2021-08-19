def invite_more_women(arr):
    if len(arr) in range(2, 51):
        count = 0
        for i in arr:
            count += i
        if count > 0:
            return True
        else:
            return False
    else:
        return False
