def well(x):
    for i in x:
        if x.count('good') >= 3:
            return 'I smell a series!'
        elif 0 < x.count('good') <= 2:
            return 'Publish!'
        elif x.count:
            return 'Fail!'

