def calculator(x,y,op):
    signs = ['+', '-', '*', '/']
    if op not in signs or type(x) == str or type(y) == str:
        return "unknown value"
    else:
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        else:
            return x / y

