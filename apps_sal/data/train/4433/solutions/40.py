from functools import reduce


def logical_calc(array, op):
    return all(array) if op == 'AND' else any(array) if op == 'OR' else reduce(lambda x, y: x != y, array)
