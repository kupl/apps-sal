def basic_op(o, v1, v2):
    return int.__dict__[{'+': '__add__', '-': '__sub__', '*': '__mul__', '/': '__truediv__'}[o]](v1, v2)
