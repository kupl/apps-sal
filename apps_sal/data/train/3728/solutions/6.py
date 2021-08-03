def describeList(list):
    if not list:
        return 'empty'
    if len(list) == 1:
        return 'singleton'
    if len(list) > 1:
        return 'longer'
