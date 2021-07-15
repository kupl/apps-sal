import functools
def logical_calc(array, op):
    if op == "AND":
        return functools.reduce(lambda prev, curr: prev and curr, array)
    if op == "OR":
        return functools.reduce(lambda prev, curr: prev or curr, array)
    if op == "XOR":
        return functools.reduce(lambda prev, curr: prev ^ curr, array)
