def well(x):
    k = 0
    for i in x:
        if i == 'good':
            k += 1
    if k == 0:
        return 'Fail!'
    if k == 1 or k == 2:
        return 'Publish!'
    if k > 2:
        return 'I smell a series!'
