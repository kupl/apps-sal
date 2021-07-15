def is_divide_by(number, a, b):
    check = True    #set true or false
    c = number % a    #div 
    d = number % b
    if c or d != 0:    #check 
        check = False
    else:
        check = True
    return check    #return true or false
        

