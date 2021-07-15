def logical_calc(arr, op):
    return all(arr) if op == 'AND' else any(arr) if op == 'OR' else arr.count(True) % 2
