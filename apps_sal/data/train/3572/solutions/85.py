def invite_more_women(arr):
    m = 0
    w = 0
    for i in arr:
        if i == 1:
            m += 1
        else:
            w += 1
    if w < m:
        return True
    return False
