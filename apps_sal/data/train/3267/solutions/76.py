def well(x):
    return 'Publish!' if 1 <= x.count('good') <= 2 else 'I smell a series!' if \
        x.count('good') > 2 else 'Fail!'
