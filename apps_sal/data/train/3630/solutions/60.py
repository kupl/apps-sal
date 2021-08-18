def arithmetic(a, b, operator):

    table = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}

    return eval(str(a) + table[operator] + str(b))
