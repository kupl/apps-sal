def logical_calc(array, op):
    return eval(f" {(op.lower() if op != 'XOR' else '^')} ".join(map(str, array)))
