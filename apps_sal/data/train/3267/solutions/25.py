def well(x):
    return {0: 'Fail!', 1: 'Publish!', 2: 'Publish!'}.get(x.count('good'), 'I smell a series!')
