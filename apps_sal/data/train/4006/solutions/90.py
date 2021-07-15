def basic_op(operator, value1, value2):
    if operator == '+':
        summary = value1 + value2
        return summary
    if operator == '-':
        summary = value1 - value2
        return summary
    if operator == '*':
        summary = value1 * value2
        return summary
    if operator == '/':
        summary = value1 / value2
        return summary
    return None
