def calculator(x, y, op):
    numbers_ok = isinstance(x, int) and isinstance(y, int)
    operator_ok = isinstance(op, str) and op in '+-*/'
    return eval(f'{x} {op} {y}') if numbers_ok and operator_ok else 'unknown value'
