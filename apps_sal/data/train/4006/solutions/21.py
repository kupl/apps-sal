import operator


def basic_op(operatorchar, value1, value2):
    return {'+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '%': operator.mod,
            '^': operator.xor
            }[operatorchar](value1, value2)
