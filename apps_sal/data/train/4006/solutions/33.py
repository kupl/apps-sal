def basic_op(operator, value1, value2):
    op = {
        '+': int.__add__,
        '-': int.__sub__,
        '*': int.__mul__,
        '/': int.__truediv__
    }
    return op[operator](value1, value2)
