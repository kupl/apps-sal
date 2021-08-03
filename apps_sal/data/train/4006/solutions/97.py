import operator


def basic_op(operator, value1, value2):
    s = str(value1) + operator + str(value2)
    return eval(s)
