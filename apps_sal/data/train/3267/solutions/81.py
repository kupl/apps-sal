def well(x):
    c = x.count('good')
    a = ''
    if c == 0:
        a = 'Fail!'
    elif c < 3:
        a = 'Publish!'
    else:
        a = 'I smell a series!'
    return a
