def well(x):
    NG = 0
    for i in range(len(x)):
        if x[i] == 'good':
            NG += 1
    if NG > 2:
        return 'I smell a series!'
    elif NG >= 1:
        return 'Publish!'
    else:
        return 'Fail!'
