def basic_op(operator, value1, value2):
    if operator in '+':
        return value1 + value2
    elif operator in '-':
        return value1 - value2
    elif operator in '*':
        return value1 * value2
    elif operator in '/':
        return value1 / value2
    else:
        pass
