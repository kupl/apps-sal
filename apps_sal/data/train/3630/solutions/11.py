def arithmetic(a, b, operator):
    op = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}
    return eval(str(a) + op[operator] + str(b))
