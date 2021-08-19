def well(x):
    good_count = 0
    for idea in x:
        if idea == 'good':
            good_count += 1
    if good_count == 0:
        return 'Fail!'
    elif good_count < 3:
        return 'Publish!'
    else:
        return 'I smell a series!'
