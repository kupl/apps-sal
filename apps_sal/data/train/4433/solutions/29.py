def logical_calc(array, op):
    if op == "AND":
        return all(boolian for boolian in array)
    elif op == "OR":
        return any(boolian for boolian in array)
    else:
        return sum(array) % 2
