def logical_calc(array, op):
    return eval(' {} '.format({'AND': 'and', 'OR': 'or'}.get(op, '^')).join((str(x) for x in array)))
