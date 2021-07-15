def is_divide_by(number, a, b):
    result_a = None
    result_b = None
    
    if a is 1:
        result_a = True
    else:
        if number % a is 0:
            result_a = True
        else:
            result_a = False
            
    if b is 1:
        result_b = True
    else:
        if number % b is 0:
            result_b = True
        else:
            result_b = False
        
    return result_a and result_b
