def calculator(x, y, op):
    d = '0123456789'
    s = '+-*/'
    if str(x) not in d or str(y) not in d or op not in s:
        return 'unknown value'
    elif op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    else:
        return x / y
