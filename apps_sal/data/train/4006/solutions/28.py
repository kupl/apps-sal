def basic_op(operator, value1, value2):
    a = int(value1)
    b = int(value2)
    if operator == "+":
        output = a + b
    elif operator == "-":
        output = a - b
    elif operator == "*":
        output = a * b
    else:
        output = a / b
    return output
