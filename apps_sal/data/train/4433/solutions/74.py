import functools

def logical_calc(array, op):
    arr = {
        "AND":lambda a,b: a and b,
        "OR":lambda a,b: a or b,
        "XOR":lambda a,b: a != b
    }
    return functools.reduce(arr[op],array)
