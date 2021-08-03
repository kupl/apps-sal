def arithmetic(a, b, operator):
    return eval('a{}b'.format({'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}[operator]))
