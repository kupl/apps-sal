def arithmetic(a, b, operator):
    try:
        x = {"add": a + b, "subtract": a - b, "divide": a / b, "multiply": a * b}
        return x.get(operator)
    except:
        return None
