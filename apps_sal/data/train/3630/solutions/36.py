def arithmetic(a, b, o):
    return eval(str(a) + {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}[o] + str(b))
