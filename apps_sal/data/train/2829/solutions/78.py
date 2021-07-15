def array_madness(a,b):
    suma = 0
    sumb = 0
    
    for i in a:
        suma = suma+i**2
        
    for i in b:
        sumb = sumb+i**3
        
        
    return suma>sumb
