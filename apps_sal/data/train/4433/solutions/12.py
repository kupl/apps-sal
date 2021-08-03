ops = {'AND': '&', 'OR': '|', 'XOR': '^'}


def logical_calc(array, op):
    return bool(eval(ops[op].join([str(int(i)) for i in array])))
