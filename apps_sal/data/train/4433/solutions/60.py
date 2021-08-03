def logical_calc(array, op):
    print(array, op)
    if op == 'AND':
        return False not in array
    if op == 'OR':
        return True in array or (True in array and False in array)
    if op == 'XOR':
        return array.count(True) % 2 != 0 or (True in array and array.count(False) % 2 != 0)
