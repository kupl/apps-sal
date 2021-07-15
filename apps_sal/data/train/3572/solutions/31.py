def invite_more_women(arr):
    a = []
    b = []
    for i in arr:
        if i < 0:
            b.append(i)
        else:
            a.append(i)
    if len(b) < len(a):
        return True
    else:
        return False
