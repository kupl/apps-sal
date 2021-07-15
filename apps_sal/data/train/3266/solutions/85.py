import math
def my_first_kata(a,b):
    is_number = bool
    if_is_number = 1
    if type(a) != int or type(b) != int: 
        is_number = False
    else:
        if_is_number = int(a) % int(b) ++ int(b) % int(a)
        
    if is_number == False:
        return is_number
    else:
        return if_is_number
