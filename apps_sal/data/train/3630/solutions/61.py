def arithmetic(a, b, operator):
    return eval(f'{a}{ {"add":"+", "subtract":"-", "multiply":"*", "divide":"/"}.get(operator) }{b}')
