def calculator(x,y,op):
    x = str(x)
    y = str(y)
    op = str(op)
    if x.isdigit() and y.isdigit():
        if op == '+':
            return int(x) + int(y)
        elif op == '-':
            return int(x) - int(y)
        elif op == '*':
            return int(x) * int(y)
        elif op == '/':
            return int(x) / int(y)
        else:
            return 'unknown value'
    else:
        return 'unknown value'

