def arithmetic(a, b, operator):
    c = 0
    if operator == 'add':
        c = a + b
    elif operator == 'multiply':
        c = a * b
    elif operator == 'divide':
        c = a / b
    elif operator == 'subtract':
        c = a - b
    return c
