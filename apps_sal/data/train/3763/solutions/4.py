def calculator(x,y,op):
    if op == '+' and type(x) == int and type(y) == int:
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    if op == '/':
        return x / y
    else:
        return 'unknown value'
