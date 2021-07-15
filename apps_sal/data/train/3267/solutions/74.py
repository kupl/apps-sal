def well(x):
    c = x.count('good')
    if 2 >= c >= 1:
        return 'Publish!'
    if c > 2:
        return 'I smell a series!'
    return 'Fail!'
