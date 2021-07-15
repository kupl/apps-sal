def well(x):
    count = 0
    for i in x:
        if i == 'good':
            count += 1
    if count > 2:
        return 'I smell a series!'
    elif count != 0:
        return 'Publish!'
    return 'Fail!'

