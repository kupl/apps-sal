def logical_calc(array, op):

    return eval({'AND': '&', 'OR': '|'}.get(op, '^').join(str(i) for i in array))
