def well(x):
    pos = x.count('good')
    if pos == 1 or pos == 2:
        return 'Publish!'
    elif pos > 2:
        return 'I smell a series!'
    else:
        return 'Fail!'
