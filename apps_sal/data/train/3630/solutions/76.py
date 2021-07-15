def arithmetic(a, b, operator):
    return operations[operator](a, b)
    
    
    
operations = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b
}
