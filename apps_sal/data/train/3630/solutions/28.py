def arithmetic(a, b, operator):
    return (lambda a, b, operator:
            (operator == "add" and a + b) or
    (operator == "subtract" and a - b) or
    (operator == "multiply" and a * b) or
        (operator == "divide" and a / b))(a, b, operator)
