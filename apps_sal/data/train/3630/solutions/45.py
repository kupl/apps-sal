def arithmetic(a, b, operator):
    op = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}
    if b == 0 and operator == 'divide':
        return 'Error! Division by zero!'
    return eval(f'{a} {op[operator]} {b}') if operator in op else 'Error! Wrong operator!'
