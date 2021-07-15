def calculate(num1, operation, num2): 
    try: 
        return eval(str(num1) + operation + str(num2))
    except: 
        return None
