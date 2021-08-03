def logical_calc(array, op):
    out = array.pop(0)
    for x in array:
        out = {'AND': x & out, 'OR': x | out, 'XOR': x ^ out}[op]
    return out
