def well(x):
    good = x.count('good')
    print (good)
    if good == 0:
        return 'Fail!'
    elif good > 2:
        return 'I smell a series!'
    else:
        return 'Publish!'
