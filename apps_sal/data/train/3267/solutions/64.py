def well(x):
    good_count = x.count('good')
    return 'I smell a series!' if good_count > 2 else 'Publish!' if good_count else 'Fail!'
