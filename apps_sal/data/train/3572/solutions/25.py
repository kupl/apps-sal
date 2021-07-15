def invite_more_women(arr):
    l=len(arr)
    sl=''.join(x for x in str(arr))
    l_1=sl.count('-1')
    if l_1<(l-l_1):
        return True
    else:
        return False
