import operator


def basic_op(oper, value1, value2):
    d = {'-': operator.sub, '+': operator.add, '*': operator.mul, '/': operator.truediv}
    return d[oper](value1, value2)
