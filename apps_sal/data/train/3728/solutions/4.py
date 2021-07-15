def describeList(lst):
    if lst:
        if len(lst) == 1:
            return 'singleton'
        return 'longer'
    return 'empty'
