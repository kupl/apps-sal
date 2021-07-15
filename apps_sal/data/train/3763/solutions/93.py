def calculator(x,y,op):
    if isinstance(x, (float, int)) == True and isinstance(y, (float, int)) == True:
        if op == '+':
            return (x + y)
        elif op == '-':
            return (x - y)
        elif op == '*':
            return (x * y)
        elif op == '/':
            return (x / y)
        elif op not in ['+', '-', '*', '/']:
            return('unknown value')
    else:
        return('unknown value')

