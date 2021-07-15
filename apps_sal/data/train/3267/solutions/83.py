def well(x):
    a = x.count('good')
    if 1 <= a <= 2:
        return 'Publish!'
    if 3 <= a:
        return 'I smell a series!'
    else: 
        return 'Fail!'
