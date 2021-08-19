def logical_calc(array, op):
    return {'AND': all(array), 'OR': any(array)}.get(op) if op != 'XOR' else __import__('functools').reduce(lambda x, y: x ^ y, array)
