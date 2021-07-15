def check_digit(n, i, j, d):
    '''
    check = str(n)[min(i,j):max(i,j)+1]
    
    if str(d) in check:
        return True
    return False
    '''
    
    return True if str(d) in str(n)[min(i,j):max(i,j)+1] else False
    

