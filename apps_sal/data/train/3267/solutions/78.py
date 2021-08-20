def well(x):
    res = ''
    if x.count('good') == 1 or x.count('good') == 2:
        res = 'Publish!'
    elif x.count('good') > 2:
        res = 'I smell a series!'
    else:
        res = 'Fail!'
    return res
