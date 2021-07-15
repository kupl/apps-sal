def logical_calc(array, op):
    if op == 'AND':
        return not False in array
    elif op == 'OR':
        return True in array
    elif op == 'XOR':
        return (array.count(True) % 2) != 0
