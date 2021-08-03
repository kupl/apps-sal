def logical_calc(array, op):
    import functools
    if op == "AND":
        return functools.reduce(lambda i, j: i and j, array)
    elif op == "OR":
        return functools.reduce(lambda i, j: i or j, array)
    elif op == "XOR":
        return functools.reduce(lambda i, j: i ^ j, array)
