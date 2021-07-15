def well(x):
    c = x.count('good')
    return 'Publish!' if c == 1 or c == 2 else 'I smell a series!' if c > 2 else 'Fail!'
