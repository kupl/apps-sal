def describeList(lst):
    return ['empty', 'singleton', 'longer'][min(2, len(lst))]
