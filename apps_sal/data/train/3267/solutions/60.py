def well(x):
    n = x.count('good')
    return 'Fail!' if n < 1 else 'Publish!' if n < 3 else 'I smell a series!'
