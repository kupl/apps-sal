def basic_op(operator, value1, value2):
    multiplication = value1 * value2
    division = value1 / value2
    addition = value1 + value2
    subtraction = value1 - value2
    result = 0
    if operator == '*':
        result = multiplication
    if operator == '/':
        result = division
    if operator == '+':
        result = addition
    if operator == '-':
        result = subtraction
    return result
