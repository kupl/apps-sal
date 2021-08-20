def calculator(x, y, op):
    try:
        return {'*': x * y, '+': x + y, '-': x - y, '/': x / y}.get(op, 'unknown value')
    except:
        return 'unknown value'
