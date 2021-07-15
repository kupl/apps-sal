def odd_count(n):
    res=len(list(range(n-1)))/2
    if res.is_integer():
        return res 
    else:
        return res + 0.5
    
    

