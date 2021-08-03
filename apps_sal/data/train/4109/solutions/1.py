def filter_list(l):
    'return a new list with the strings filtered out'
    return [x for x in l if type(x) is not str]
