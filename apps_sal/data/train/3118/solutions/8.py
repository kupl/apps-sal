def is_lucky(n):
    print(36%9)
    res = 0 
    
    for x in str(n): 
        res += int(x)
    
    if res % 9 == 0: return True 
    else: return False 
