def calculator(x, y, o):
    if isinstance(x, int) and isinstance(y, int):
        return x + y if o == '+' else x - y if o == '-' else x * y if o == '*' else x / y if o == '/' else "unknown value"
    else:
        return "unknown value"
