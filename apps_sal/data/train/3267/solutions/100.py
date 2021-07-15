def well(x):
    # your code here
    if 'good' not in x:
        return 'Fail!'
    elif 3>x.count('good')>0:
        return 'Publish!'
    else:
        return 'I smell a series!'
