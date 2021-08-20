def calculator(x, y, op):
    if isinstance(x, int) and isinstance(y, int):
        try:
            if op == '+':
                return x + y
            elif op == '-':
                return x - y
            elif op == '*':
                return x * y
            elif op == '/':
                return x / y
            else:
                return 'unknown value'
        except:
            return 'unknown value'
    else:
        return 'unknown value'
