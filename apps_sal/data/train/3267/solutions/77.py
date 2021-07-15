def well(x):
    if 'good' not in x:
        return 'Fail!'
    good = 0
    for i in x:
        if i == 'good':
            good += 1
    if good > 2:
        return 'I smell a series!'
    return 'Publish!'
