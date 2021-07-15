def basic_op(operation, value1, value2):
    # if operator is +, add
    if operation == "+": return value1 + value2
    # if operator is -, subtract
    elif operation == "-": return value1 - value2
    # if operator is *, multiply
    elif operation == "*": return value1 * value2
    # if none of the operators match, simply divide
    else: return value1 / value2

print(basic_op('+', 4, 7))  # Output: 11
print(basic_op('-', 15, 18)) # Output: -3
print(basic_op('*', 5, 5))  # Output: 25
print(basic_op('/', 49, 7)) # Output: 7
