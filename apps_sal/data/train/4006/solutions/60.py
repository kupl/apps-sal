def basic_op(operation, value1, value2):
    if operation == "+":
        return value1 + value2
    elif operation == "-":
        return value1 - value2
    elif operation == "*":
        return value1 * value2
    else:
        return value1 / value2


print(basic_op('+', 4, 7))
print(basic_op('-', 15, 18))
print(basic_op('*', 5, 5))
print(basic_op('/', 49, 7))
