def basic_op(operator, value1, value2):
    dict = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}
    return dict[operator](value1, value2)
