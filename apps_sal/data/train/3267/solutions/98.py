def well(x):
    y = x.count('good')
    if 2 >= y >= 1:
        return 'Publish!'
    elif y >= 3:
        return 'I smell a series!'
    if y == 0:
        return 'Fail!'
