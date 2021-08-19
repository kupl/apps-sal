def well(x):
    return 'Publish!' if x.count('good') == 2 or x.count('good') == 1 else 'I smell a series!' if x.count('good') > 2 else 'Fail!'
