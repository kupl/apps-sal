import operator


ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


def basic_op(oper, value1, value2):
    return ops[oper](value1, value2)
