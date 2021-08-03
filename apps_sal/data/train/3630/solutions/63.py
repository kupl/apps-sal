def arithmetic(a, b, operator):
    if operator == 'add':
        operator = '+'
    elif operator == 'subtract':
        operator = '-'
    elif operator == 'multiply':
        operator = '*'
    elif operator == 'divide':
        operator = '/'

    return eval('{}{}{}'.format(a, operator, b))
