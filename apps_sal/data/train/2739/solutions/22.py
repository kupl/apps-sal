def cube_odd(arr):

    s = 0
    
    if any(isinstance(b,bool) for b in arr):
        
        return None
    
    if not all(isinstance(x,int) for x in arr):
        
        return None

    for i in range(0,len(arr)):
    
        if arr[i]%2!=0 :
        
            s+= arr[i]**3
               
    return s
    

