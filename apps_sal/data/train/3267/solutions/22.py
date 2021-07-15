def well(x):
    n = x.count('good')
    return ('Fail!', 'Publish!', 'I smell a series!')[(n > 0) + (n > 2)]
