def basic_op(operator, value1, value2):
    x = str(value1), operator, str(value2)
    x = eval(''.join(x))
    return x
