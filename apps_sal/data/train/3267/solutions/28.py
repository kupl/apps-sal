def well(x):
    if x.count('good') <= 2 and x.count('good') > 0:
        return 'Publish!'
    elif x.count('good') > 0:
        return 'I smell a series!'
    else:
        return 'Fail!'
