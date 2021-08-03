def capitalize(s):
    t1 = ''
    t2 = ''
    for i, j in enumerate(s):
        if i % 2 == 0:
            t1 += j.upper()
            t2 += j
        else:
            t1 += j
            t2 += j.upper()
    return [t1, t2]
