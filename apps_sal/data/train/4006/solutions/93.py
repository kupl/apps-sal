def _sum(value1, value2):
    return value1 + value2

def _substract(value1, value2):
    return value1 - value2

def _multiply(value1, value2):
    return value1 * value2

def _divide(value1, value2):
    return value1 / value2


OPERATORS_MAP = {
    "+": _sum,
    "-": _substract,
    "*": _multiply,
    "/": _divide,
}

def basic_op(operator, value1, value2):
    
    result = OPERATORS_MAP[operator](value1, value2)

    return result
