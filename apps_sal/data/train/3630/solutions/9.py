def arithmetic(a, b, operator):
    ops = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}
    return eval(str(a) + ops[operator] + str(b))
