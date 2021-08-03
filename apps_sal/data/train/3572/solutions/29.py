def invite_more_women(arr):
    w = 0
    m = 0
    for i in arr:
        if i == 1:
            m = m + 1
        else:
            w = w + 1
    if w < m:
        return True
    else:
        return False
