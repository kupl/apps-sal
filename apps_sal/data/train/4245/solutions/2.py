def explode(arr):  
    a,b,c = arr[0],arr[1],0
    if type(a) == int: c+=a
    if type(b) == int: c+=b
    if c == 0: return "Void!"    
    return [arr]*c

