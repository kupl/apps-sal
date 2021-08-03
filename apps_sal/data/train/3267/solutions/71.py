def well(x):
    g = sum([1 for item in x if item == 'good'])
    if g > 2:
        return 'I smell a series!'
    elif g > 0:
        return 'Publish!'
    else:
        return 'Fail!'
