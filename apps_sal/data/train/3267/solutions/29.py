def well(x):
    goods = x.count('good')
    return ['Fail!', 'Publish!', 'I smell a series!'][(goods > 2) + (goods >= 1)]
