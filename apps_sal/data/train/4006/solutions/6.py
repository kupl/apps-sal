def basic_op(operator, value1, value2):
    ops = {'+': lambda a, b: a + b, 
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: a / b}
    return ops[operator](value1, value2)
