def well(x):
    i = x.count('good')
    if i > 2:
        return 'I smell a series!'
    elif i == 0:
        return 'Fail!'
    else:
        return 'Publish!'
