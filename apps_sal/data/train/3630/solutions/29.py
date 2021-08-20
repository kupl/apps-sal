def arithmetic(a, b, operator):
    if operator.lower() == 'multiply':
        return eval(f'{a}*{b}')
    if operator.lower() == 'divide':
        return eval(f'{a}/{b}')
    if operator.lower() == 'add':
        return eval(f'{a}+{b}')
    if operator.lower() == 'subtract':
        return eval(f'{a}-{b}')
