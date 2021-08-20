def arithmetic(a, b, operator):
    ops = {'add': lambda a, b: a + b, 'subtract': lambda a, b: a - b, 'multiply': lambda a, b: a * b, 'divide': lambda a, b: a / b}
    return ops[operator](a, b)
