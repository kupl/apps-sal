def arithmetic(a, b, operator):
    result = 0
    if operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    elif operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = a / b
    else:
        print('No operator found')
    return result
