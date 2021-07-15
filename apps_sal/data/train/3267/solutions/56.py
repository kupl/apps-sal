def well(x):
    counter = 0
    for idea in x:
        if idea == 'good':
            counter += 1
    if counter == 0:
        return 'Fail!'
    elif counter <= 2:
        return 'Publish!'
    else:
        return 'I smell a series!'
