def scratch(lottery):

    c = 0
    
    for i in range(0,len(lottery)):
        
        lo = lottery[i].split()
        
        print(lo)
        
        if all(x == lo[0] for x in lo[0:-1]):
            
            c+= int(lo[-1])
            
    return c


