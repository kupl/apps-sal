def well(x):
    good_counter = 0
    for i in x:
        if i == 'good':
            good_counter += 1
    if 1 <= good_counter <= 2:
        return 'Publish!'
    elif good_counter > 2:
        return 'I smell a series!'
    else:
        return 'Fail!'
