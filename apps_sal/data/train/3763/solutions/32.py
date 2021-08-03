def calculator(x, y, op):
    print(x, y, op)
    lst = ['+', '-', '*', '/']
    if op not in lst:
        return "unknown value"
    if str(x).isnumeric() is False or str(y).isnumeric() is False:
        return "unknown value"
    elif op == '+':
        return int(x) + int(y)
    elif op == '-':
        return int(x) - int(y)
    elif op == '*':
        return int(x) * int(y)
    elif op == '/':
        return int(x) / int(y)
