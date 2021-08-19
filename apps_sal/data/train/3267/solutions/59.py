def well(x):
    return 'Publish!' if x.count('good') in [1, 2] else 'I smell a series!' if x.count('good') > 2 else 'Fail!'
