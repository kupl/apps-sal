def calculator(x, y, op):
    if type(x) is int and type(y) is int:
        switcher = {'+': x + y, '-': x - y, '*': x * y, '/': x / y}
        return switcher.get(op, 'unknown value')
    else:
        return 'unknown value'
