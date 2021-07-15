def logical_calc(array, op):
    if op == 'AND':
        return all(array)
    elif op == 'OR':
        return any(array)
    else:
        return array.count(True) % 2
