def arithmetic(a, b, o):
    res = 0
    if o == 'add':
        res = a + b
    elif o == 'subtract':
        res = a - b
    elif o == 'multiply':
        res = a * b
    elif o == 'divide':
        res = a / b
    else:
        res = 'Please specify operator ... '
    return res
