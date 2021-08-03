def arithmetic(a, b, operator):
    c = {"add": (a + b), "subtract": (a - b), "multiply": (a * b), "divide": (a / b)}
    return c[operator]
