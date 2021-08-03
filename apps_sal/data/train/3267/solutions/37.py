def well(x):
    if not('good' in x):
        return 'Fail!'
    else:
        return 'Publish!' if x.count('good') < 3 else 'I smell a series!'
