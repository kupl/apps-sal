def describeList(list):
    if not list:
        return 'empty'
    elif len(list) == 1:
        return 'singleton'
    return 'longer'
