def arithmetic(a, b, operator):
    res = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b
    }
    return res.get(operator, "Invalid operator")
