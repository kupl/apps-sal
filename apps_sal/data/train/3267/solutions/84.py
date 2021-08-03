def well(x):
    count = x.count('good')

    return 'Fail!' if count == 0 else 'Publish!' if count <= 2 else 'I smell a series!'
