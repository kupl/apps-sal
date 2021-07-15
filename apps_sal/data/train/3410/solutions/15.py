def scratch(lottery):
    r = 0
    for s in lottery:
        *a,b = s.split()
        if len(set(a))==1:
            r += int(b)
    return r
