def well(x):
    c = len([i for i in x if i == 'good'])
    if c == 0:
        return 'Fail!'
    elif c < 3:
        return 'Publish!'
    else:
        return 'I smell a series!'
