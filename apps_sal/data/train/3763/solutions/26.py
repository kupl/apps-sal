def calculator(x,y,op):
    if isinstance(x, int) and isinstance(y, int) and isinstance(op, str):
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
        else:
            return "unknown value"
    else:
        return "unknown value"

