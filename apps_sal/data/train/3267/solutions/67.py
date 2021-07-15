def well(x):
    l=x.count('good')
    return 'I smell a series!' if l>2 else 'Publish!' if l>0 else 'Fail!'
