def well(x):
    if x.count('bad') == len(x):
        return 'Fail!'
    if x.count('good') == 1 or x.count('good') == 2:
        return 'Publish!'
    else:
        return 'I smell a series!'
