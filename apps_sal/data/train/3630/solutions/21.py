def arithmetic(a, b, operator):
    dict = {'add': a + b, 'subtract': a - b, 'multiply': a * b, 'divide': a / b}
    return dict[operator]
