def arithmetic(a, b, operator):
    operations = {'add': lambda x: a + b, 'subtract': lambda x: a - b, 'multiply': lambda x: a * b, 'divide': lambda x: a / b}
    return operations[operator](1)
