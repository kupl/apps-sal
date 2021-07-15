def catch_sign_change(lst):
    
    result = 0
        
    for i in range(len(lst)-1):
    
        a = lst[i] if lst[i] !=0 else 1
        b = lst[i+1] if lst[i+1] !=0 else 1
        
        if a*b < 0:
            result += 1
            
    return result
