def basereduct(x):
    s = str(x)
    b = 10
    m = max(list(s))
    if m == '9':
        b = 11
    else:
        b = int(m) + 1
    k = 0
    while len(s) > 1:
        t = int(s, b)
        s = str(t)
        m = max(list(s))
        if m == '9':
            b = 11
        else:
            b = int(m) + 1
        k += 1
        if k == 200:
            break
    if k == 200:
        return -1
    return int(s, b)
