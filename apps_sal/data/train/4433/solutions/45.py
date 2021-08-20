def logical_calc(a, o):
    return __import__('functools').reduce({'AND': lambda a, b: a & b, 'OR': lambda a, b: a | b, 'XOR': lambda a, b: a ^ b}[o], a, o == 'AND')
