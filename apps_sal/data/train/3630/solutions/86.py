def arithmetic(a, b, operator):
    if operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    elif operator == 'divide':
        result = a / b
    elif operator == 'multiply':
        result = a * b
    else:
        print("You didn't enter an operator or you misspelled the operator.")
    return result
