def isDigit(string):
    
    string = string.strip()
    
    if len(string) < 1:
        return False
    
    if string[0] not in '0123456789-':
        return False
    
    index_point = -1
    
    if string.count('.') > 1:
        return False
        
    elif string.count('.') == 1:
        index_point = string.find('.')
        if string[0] == '-':
            if string[1:index_point].isdigit() and string[index_point+1:].isdigit():
                return True
            else:
                return False
        else:
            if string[0:index_point].isdigit() and string[index_point+1:].isdigit():
                return True
            else:
                return False
        
    else:    
        if string[0] == '-':
            return string[1:].isdigit()
        else:
            return string.isdigit()
