def well(x):
    chk = x.count('good')
    return ['Fail!', 'Publish!', 'I smell a series!'][(chk > 0) + (chk > 2)]
