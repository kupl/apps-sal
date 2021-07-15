def logical_calc(array, op):
    if op == "AND":
        return all(array)
    elif op == "OR":
        return any(array)
    elif op == "XOR":
        return array.count(True) % 2 != 0
