def describeList(list):
    if len(list)==1:
        return 'singleton'
    elif len(list)>1:
        return 'longer'
    else:
        return 'empty'
