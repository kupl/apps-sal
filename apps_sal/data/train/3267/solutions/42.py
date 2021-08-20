def well(x):
    num_good = x.count('good')
    if num_good == 0:
        return 'Fail!'
    elif num_good > 2:
        return 'I smell a series!'
    return 'Publish!'
