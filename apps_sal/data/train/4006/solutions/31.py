def basic_op(operator, value1, value2):
    return {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b, '/': lambda a, b: a / b}[operator](value1, value2)
