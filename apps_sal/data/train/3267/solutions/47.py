def well(x):
    c = 0
    for i in x:
        if i == 'good':
            c += 1

    if c == 1 or c == 2:
        return 'Publish!'
    elif c > 2:
        return 'I smell a series!'
    elif c == 0:
        return 'Fail!'
