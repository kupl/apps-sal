def cube_odd(arr):
    for x in arr:
        if type(x) is not int:
            return None
    
    cube = [x **3 for x in arr]
    r = 0
    for x in cube:
        if x % 2 != 0:
            r += x
    return r
    # Flez
  
      
    

