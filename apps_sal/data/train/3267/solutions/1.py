def well(x):
    if x.count('good') == 0:
        return 'Fail!'
    elif x.count('good') <= 2:
        return 'Publish!'
    else:
        return 'I smell a series!'
