import operator


def arithmetic(a, b, operator_name):
    operators = {'add': operator.add, 'subtract': operator.sub, 'multiply': operator.mul, 'divide': operator.truediv}
    return operators[operator_name](a, b)
