def well(x):
    c = x.count('good')
    if 0 < c <= 2:
        return 'Publish!'
    elif c > 2:
        return 'I smell a series!'
    else:
        return 'Fail!'
