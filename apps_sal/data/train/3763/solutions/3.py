def calculator(x, y, op):
    if isinstance(x, int) and isinstance(y, int):
        op_dict = {'+': x + y, '-': x - y, '*': x * y, '/': x / y}
        return op_dict[op] if op in op_dict else 'unknown value'
    return 'unknown value'
