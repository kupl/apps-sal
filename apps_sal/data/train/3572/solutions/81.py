def invite_more_women(arr):
    sumInput = sum(arr)
    if sumInput < 0:
        return False
    elif sumInput == 0:
        return False
    else:
        return True
