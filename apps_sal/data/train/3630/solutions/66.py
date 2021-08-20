def arithmetic(a, b, operator):
    result = 0
    if operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b
    elif operator == 'multiply':
        return a * b
    else:
        return a / b
