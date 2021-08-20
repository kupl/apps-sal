def logical_calc(array, op):
    if False in array and op == 'AND':
        return False
    elif op == 'AND':
        return True
    elif True in array and op == 'OR':
        return True
    elif op == 'OR':
        return False
    elif int(array.count(True)) % 2 == 0 and int(array.count(False)) % 2 == 0 and (op == 'XOR'):
        return False
    elif int(array.count(True)) % 2 == 1 and op == 'XOR':
        return True
    elif int(array.count(False)) % 2 == 1 and int(array.count(True)) % 2 == 1 and (op == 'XOR'):
        return False
    elif int(array.count(False)) % 2 == 1 and op == 'XOR':
        return False
