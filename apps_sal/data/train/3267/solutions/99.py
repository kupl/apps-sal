def well(x):
    if not 'good' in x:
        return 'Fail!'
    else:
        if len([i for i in x if i=="good"])>2:
            return 'I smell a series!'
        else:
            return 'Publish!'
