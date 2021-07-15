def well(x):
    if x.count('good') > 2:
        return 'I smell a series!'
    if 'good' in x:
        return 'Publish!'
    return 'Fail!'
