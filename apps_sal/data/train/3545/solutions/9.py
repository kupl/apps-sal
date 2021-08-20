def well(arr):
    s = []
    for x in arr:
        s += x
    a = []
    for c in s:
        if isinstance(c, str):
            a.append(c)
    cpt = 0
    for w in a:
        if w.lower() == 'good':
            cpt += 1
    if cpt > 2:
        return 'I smell a series!'
    if 0 < cpt < 3:
        return 'Publish!'
    return 'Fail!'
