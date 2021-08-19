def arithmetic(a, b, operator):
    calc = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}
    return eval(str(a) + calc[operator] + str(b))
