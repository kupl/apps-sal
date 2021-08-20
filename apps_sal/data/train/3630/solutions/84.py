def arithmetic(a, b, operator):
    ops = {'add': '__add__', 'subtract': '__sub__', 'multiply': '__mul__', 'divide': '__truediv__'}
    return getattr(a, ops[operator])(b)
