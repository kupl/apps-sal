def well(x):
    temp = x.count("good")
    if 0 < temp < 3:
        return 'Publish!'
    elif temp > 2:
        return 'I smell a series!'
    else:
        return 'Fail!'
