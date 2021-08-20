def logical_calc(arr, op):
    return eval((' ^ ' if op == 'XOR' else ' ' + op.lower() + ' ').join((str(x) for x in arr)))
