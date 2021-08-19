def invite_more_women(arr):
    # your code here
    sumInput = sum(arr)
    if sumInput < 0:
        return False
    elif sumInput == 0:
        return False
    else:
        return True
