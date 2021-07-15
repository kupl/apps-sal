def basic_op(operator, value1, value2):
    if operator == '+':
        result = value1 + value2
    elif operator == '-':
        result = value1 - value2
    elif operator == '*':
        result = value1 * value2
    elif operator == '/':
        result = value1 / value2
    else:
        result = None
    return result
    

