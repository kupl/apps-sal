def well(x):
    return ('Fail!', 'Publish!', 'I smell a series!')[('good' in x) + (x.count('good') > 2)]
