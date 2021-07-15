def logical_calc(array, op):
    if op == 'AND':
        return array.count(False) == 0
    elif op == 'OR':
        return array.count(True) != 0
    else:
        return array.count(True) % 2 == 1
