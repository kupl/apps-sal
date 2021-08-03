import distutils


def quick_op(op, old, new):
    if op == "AND":
        return old and new
    elif op == "OR":
        return old or new
    elif op == "XOR":
        return old ^ new


def logical_calc(array, op):
    latest_operation = array[0]
    array.pop(0)
    for item in array:
        latest_operation = quick_op(op, latest_operation, item)
    return latest_operation
