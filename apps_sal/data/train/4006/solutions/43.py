def basic_op(operator, value1, value2):
    return {'+': value1 + value2, '-': value1 - value2, '*': value1 * value2, '/': value1 / value2}.get(operator)
