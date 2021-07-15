def arithmetic(a, b, operator):
    if operator.lower() == "add":
        return a + b
    elif operator.lower() == "subtract":
        return a - b
    elif operator.lower() == "multiply":
        return a*b
    else:
        return a/b
