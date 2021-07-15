def asterisc_it(n): 
    if isinstance(n, list):
        for i in range(len(n)):
            n[i] = str(n[i])
        n_str = ''.join(n)
    else:
        n_str = str(n)
        
    prev = False
    result = ""
    
    for s in n_str:
        if int(s) % 2 == 0:
            if prev == True:
               result = result + '*' 
            prev = True
        else:
            prev = False
        result = result + s
        
    return result
