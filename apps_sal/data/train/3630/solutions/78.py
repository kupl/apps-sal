def arithmetic(a, b, operator):
    total = 0
    if operator == "add":
        total = a + b
    elif operator == "subtract":
        total = a - b
    elif operator == "multiply":
        total = a * b
    elif operator == "divide":
        total = a / b
    else:
        return "Something Went Wrong"
    return total
