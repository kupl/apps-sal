def basic_op(operator, value1, value2):
    if operator == '+' and type(value1) == int and (type(value2) == int):
        return value1 + value2
    if operator == '-':
        return value1 - value2
    if operator == '*':
        return value1 * value2
    else:
        return value1 / value2
