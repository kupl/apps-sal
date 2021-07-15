def arithmetic(a, b, operator):
    return getattr(a, '__' + operator[:3] + '__', a.__truediv__)(b)
