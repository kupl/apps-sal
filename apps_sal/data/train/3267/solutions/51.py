def well(x):
    c = x.count('good')
    return ('Publish!' if c <= 2 else 'I smell a series!') if c>0 else 'Fail!'
