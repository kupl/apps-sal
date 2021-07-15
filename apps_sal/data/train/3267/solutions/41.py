def well(x):
    v = len([i for i in x if i == 'good'])
    return 'Fail!' if v == 0 else 'I smell a series!' if v > 2 else 'Publish!'
