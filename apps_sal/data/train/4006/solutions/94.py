def basic_op(operator, value1, value2):
    #your code here
    operator == str(operator)
    value1 == float(value1)
    value2 == float(value2)
    if operator == '+':
        addition = float(value1 + value2)
        return addition
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    else:
        division = value1/value2
        return division
