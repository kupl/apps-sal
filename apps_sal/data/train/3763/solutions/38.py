def calculator(x,y,op):
    pass
    if type(x) != int or type(y) != int:
        return "unknown value"
    while op not in ['+', '-', '*', '/']:
        return "unknown value"
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    if op == '/':
        return x / y

