def arithmetic(a, b, operator):
    switcher = {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b,
    }
    return switcher[operator]
