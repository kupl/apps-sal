def isNumber(char):
    if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        
        return True
    else:
        return False

def solve(s):
    
    max_number = 0
    
    new_number = []
        
    for char in s:
        
        if isNumber(char):
            
            new_number.append(char)
            
        else:

            if new_number != []: # if there is a number to be compared:                
                k = int(''.join(new_number))
                if k > max_number:
                    max_number = k
                    
            new_number = []
            

    # and for the last char:
    if new_number != []: # if there is a number to be compared:                
        k = int(''.join(new_number))
        if k > max_number:
            max_number = k
                    
    return max_number
