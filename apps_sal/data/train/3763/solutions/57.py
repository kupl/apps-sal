def calculator(x, y, op):
    return eval(f'{x} {op} {y}') if op in ['+', '-', '*', '/'] and isinstance(x, int) and isinstance(y, int) else 'unknown value'
