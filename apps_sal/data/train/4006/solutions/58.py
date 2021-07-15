from operator import add, sub, mul, truediv

def basic_op(operator, value1, value2):
    ops = {"+": add, "-": sub, "*": mul, "/": truediv}
    return ops.get(operator)(value1, value2)
