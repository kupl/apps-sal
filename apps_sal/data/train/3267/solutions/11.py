def well(x):
    y = 0
    for c in x:
        if c == 'good':
            y = y + 1
    if y == 0:
        return 'Fail!'
    if y > 2:
        return 'I smell a series!'
    return 'Publish!'
