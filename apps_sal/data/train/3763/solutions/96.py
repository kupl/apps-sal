def calculator(x, y, op):
    if type(x) != int or type(y) != int:
        return('unknown value')
    elif op == '/':
        return(x / y)
    elif op == '*':
        return(x * y)
    elif op == '-':
        return(x - y)
    elif op == '+':
        return(x + y)
    else:
        return('unknown value')
    pass
