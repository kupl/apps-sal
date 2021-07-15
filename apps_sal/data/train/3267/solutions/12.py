def well(x):
    if x.count('good') >= 3:
        return 'I smell a series!'
    elif x.count('good') >= 1:
        return 'Publish!'
    return 'Fail!'

