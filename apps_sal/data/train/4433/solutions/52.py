from functools import reduce


def logical_calc(array, op):
    oper = op.lower() if op != 'XOR' else '^'
    return reduce(lambda x, y: eval(f'{x} {oper} {y}'), array)
