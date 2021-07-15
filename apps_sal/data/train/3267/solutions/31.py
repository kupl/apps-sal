def well(x):
    print(x)
    if 0 < x.count('good') <= 2: return 'Publish!'
    elif x.count('good') > 2: return 'I smell a series!'
    else: return 'Fail!'
