def arithmetic(a, b, operator):
    formats = {
        "add": a + b,
        "subtract": a - b,
        "divide": a / b,
        "multiply": a * b
    }

    return formats.get(operator)
