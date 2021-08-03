def well(x):
    y = x.count('good')
    if y is 0:
        return "Fail!"
    if y == 1 or y == 2:
        return "Publish!"
    return 'I smell a series!'
