def well(x):
    g=x.count('good')
    if g>2: return 'I smell a series!'
    if g: return 'Publish!'
    return 'Fail!'
