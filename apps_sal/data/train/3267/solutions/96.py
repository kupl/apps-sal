def well(x):
    goodCounter = 0
    for i in range(len(x)):
        if x[i] == 'good':
            goodCounter += 1
    if goodCounter == 1 or goodCounter == 2:
        return 'Publish!'
    elif goodCounter > 2:
        return 'I smell a series!'

    return 'Fail!'
