def arithmetic(a, b, operator):
    ops = {"add": lambda x, y: x + y,
           "subtract": lambda x, y: x - y,
           "multiply": lambda x, y: x * y,
           "divide": lambda x, y: float(x) / y,
           }
    return ops[operator](a, b)
