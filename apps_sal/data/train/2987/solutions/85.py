def is_divide_by(number, a, b):
    n = number / a 
    m = number / b
    
    if n.is_integer() == True and m.is_integer() == True:
        return True
    else:
        return False
    

