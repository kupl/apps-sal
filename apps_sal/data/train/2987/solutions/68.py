def is_divide_by(number, a, b):
    return not abs(number) % abs(a) | abs(number) % abs(b)
