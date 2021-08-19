operations = {'*': lambda value1, value2: value1 * value2, '-': lambda value1, value2: value1 - value2, '/': lambda value1, value2: value1 / value2, '+': lambda value1, value2: value1 + value2}


def basic_op(operator, value1, value2):
    return operations[operator](value1, value2)
