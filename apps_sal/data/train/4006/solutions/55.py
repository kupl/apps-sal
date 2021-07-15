# function takes two numbers and basic math operator character to perform on the numbers
def basic_op(operator, value1, value2):
    # series of if statements to determine basic operator and return result
    if operator == '+': return value1 + value2
    elif operator == '-': return value1 - value2
    elif operator == '*': return value1 * value2
    elif operator == '/': return value1 / value2
