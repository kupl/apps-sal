def logical_calc(array, op):
    ops = {'XOR': ' ^ ',
           'AND': ' and ',
           'OR': ' or '}

    return eval(ops[op].join([str(v) for v in array]))
