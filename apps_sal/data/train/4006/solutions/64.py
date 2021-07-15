def basic_op(operator, value1, value2):
    arr = [str(value1), operator, str(value2)]
    return eval(''.join(arr))
