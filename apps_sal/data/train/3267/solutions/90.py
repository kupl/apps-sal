def well(x):
    good = x.count('good')
    if good > 2:
        return 'I smell a series!'
    elif good == 0:
        return 'Fail!'
    else:
        return 'Publish!'
