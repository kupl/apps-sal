def arithmetic(a, b, operator):
    return {
        'add': lambda a, b: a + b,
        'subtract': lambda a, b: a - b,
        'multiply': lambda a, b: a * b,
        'divide': lambda a, b: a / b
    }[operator](a, b)
