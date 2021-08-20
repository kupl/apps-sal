def logical_calc(array, op):
    s = ' ' + op.lower().replace('xor', '^') + ' '
    return eval(s.join((str(x) for x in array)))
