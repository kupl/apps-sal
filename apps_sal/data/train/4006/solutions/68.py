def basic_op(operator, value1, value2):
    switch = {
        '+': value1 + value2,
        '-': value1 - value2,
        '*': value1 * value2,
        '/': value1 / value2,
    }
    return switch.get(operator, "Invalid Operator")

