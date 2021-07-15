def arithmetic(a, b, operator):
    #your code here
    
    table = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/" }
    
    return eval(str(a) + table[operator] + str(b))
