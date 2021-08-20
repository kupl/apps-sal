def basic_op(operator, value1, value2):
    ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}
    return ops[operator](value1, value2)
