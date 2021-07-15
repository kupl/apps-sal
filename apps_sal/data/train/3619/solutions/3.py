def is_dd(n):
    lstr = list(str(n))
    dds = 0
    
    for x in lstr:
        numdigits = 0;
        
        for y in lstr:
            if y == x:
                numdigits += 1
        if numdigits == int(x):
            return True
            
    return False
            

