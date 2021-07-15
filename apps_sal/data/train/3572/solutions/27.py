def invite_more_women(arr):
    nm = len([x for x in arr if x == 1])
    nw = len([x for x in arr if x == -1])
    if nw < nm:
        return True
    else:
        return False
