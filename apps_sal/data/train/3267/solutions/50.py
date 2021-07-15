def well(x):
    a = 0
    for i in x:
        if i.lower() == 'good':
            a += 1
    if a <= 2 and a != 0:
        return 'Publish!'
    elif a > 2:
        return 'I smell a series!'
    else:
        return 'Fail!'
