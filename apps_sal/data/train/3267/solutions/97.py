def well(x):
    if str(x.count('good')) in '12':
        return 'Publish!'
    elif x.count('good') > 2:
        return 'I smell a series!'
    else:
        return 'Fail!'
